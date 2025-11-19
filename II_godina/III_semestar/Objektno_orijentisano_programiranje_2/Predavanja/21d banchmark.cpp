#include <iostream>
#include <chrono>
#include <cmath>
#include <random>

#include <tuple>
#include <variant>

constexpr int k_numOfShapes = 500'000;
constexpr unsigned int k_randSeed = 5;


struct Point
{
	int x, y;
	Point(int xx, int yy) : x(xx), y(yy) { }
	Point() :x(0), y(0) { }
};


namespace oop_style {
struct Shape
{
	virtual double perimeter() =0;
};

struct Line : Shape
{
	Line(Point a, Point b) : m_a(a), m_b(b) {}

	double perimeter() override {
		int x = std::abs(m_a.x - m_b.x);
		int y = std::abs(m_a.y - m_b.y);
		return std::sqrt(x*x + y*y);
	}

private:
	Point m_a;
	Point m_b;
};

struct Rectangle : Shape
{
	Rectangle(Point x, int w, int h) : m_x(x), m_w(w), m_h(h) {}
	Rectangle(Point a, Point b) : m_x(a), m_w(b.x - a.x), m_h(b.y - a.y) {}

	double perimeter() override { return 2 * (m_w + m_h); }

private:
	Point m_x;
	int m_w;
	int m_h;
};

struct Circle : Shape
{
	Circle(Point x, int r) : m_x(x), m_r(r) {}

	double perimeter() override { return 2 * m_r * M_PI; }

private:
	Point m_x;
	int m_r;
};



struct Canvas {
	void addShape(Shape* x) { m_v.push_back(x); }

	double totalPerimeter() {
		double s{0.0};
		for (auto& it : m_v)
			s += it->perimeter();
		return s;
	}

private:
	std::vector<Shape*> m_v;
};

void populate(Canvas& canvas)
{
	std::mt19937 gen(k_randSeed);
	std::uniform_int_distribution<> shapeChoice(1, 3);
	std::uniform_int_distribution<> lc(1, 20);

	for (int i = 0; i < k_numOfShapes; ++i) {
		switch (shapeChoice(gen)) {
			case 1: {
				canvas.addShape(new Line({lc(gen), lc(gen)}, {lc(gen), lc(gen)}));
			}
			break;
			case 2: {
				canvas.addShape(new Rectangle({lc(gen), lc(gen)}, lc(gen), lc(gen)));
			}
			break;
			case 3: {
				canvas.addShape(new Circle({lc(gen), lc(gen)}, lc(gen)));
			}
			break;
		}
	}
}

Canvas g_canvas;

double g_x;
}

static void ooVersion(benchmark::State& state) {
	oop_style::populate(oop_style::g_canvas);
	double x{0.0};
	// Code before the loop is not measured
	for (auto _ : state) {
		x += oop_style::g_canvas.totalPerimeter();
	}
	oop_style::g_x = x;
}
BENCHMARK(ooVersion);


//
//--------------------------------------------------------------
//


namespace variant_style
{
struct Line
{
	Line(Point a, Point b) : m_a(a), m_b(b) {}

	double perimeter() {
		int x = std::abs(m_a.x - m_b.x);
		int y = std::abs(m_a.y - m_b.y);
		return std::sqrt(x*x + y*y);
	}

private:
	Point m_a;
	Point m_b;
};

struct Rectangle
{
	Rectangle(Point x, int w, int h) : m_x(x), m_w(w), m_h(h) {}
	Rectangle(Point a, Point b) : m_x(a), m_w(b.x - a.x), m_h(b.y - a.y) {}

	double perimeter() { return 2 * (m_w + m_h); }

private:
	Point m_x;
	int m_w;
	int m_h;
};

struct Circle
{
	Circle(Point x, int r) : m_x(x), m_r(r) {}

	double perimeter() { return 2 * m_r * M_PI; }

private:
	Point m_x;
	int m_r;
};



// Canvas that can hold: Line, Rectangle, Circle


template<typename... Ts>
struct Canvas {
	using ShapesVar = std::variant<Ts...>;

	void addShape(ShapesVar x) { m_v.push_back(x); }

	double totalPerimeter() {
		double x{0.0};
		for (auto& it : m_v)
			x += std::visit([](auto x){ return x.perimeter(); }, it);
		return x;
	}

private:
	std::vector<ShapesVar> m_v;
};

void populate(Canvas<Line, Rectangle, Circle>& canvas)
{
	std::mt19937 gen(k_randSeed);
	std::uniform_int_distribution<> shapeChoice(1, 3);
	std::uniform_int_distribution<> lc(1, 20);

	for (int i = 0; i < k_numOfShapes; ++i) {
		switch (shapeChoice(gen)) {
			case 1: {
				canvas.addShape(Line({lc(gen), lc(gen)}, {lc(gen), lc(gen)}));
			}
			break;
			case 2: {
				canvas.addShape(Rectangle({lc(gen), lc(gen)}, lc(gen), lc(gen)));
			}
			break;
			case 3: {
				canvas.addShape(Circle({lc(gen), lc(gen)}, lc(gen)));
			}
			break;
		}
	}
}

Canvas<Line, Rectangle, Circle> g_canvas;

double g_x;
}

static void variantVersion(benchmark::State& state) {
	variant_style::populate(variant_style::g_canvas);
	double x{0.0};
	// Code before the loop is not measured
	for (auto _ : state) {
		x += variant_style::g_canvas.totalPerimeter();
	}
	variant_style::g_x = x;
}
BENCHMARK(variantVersion);


//
//--------------------------------------------------------------
//


namespace data_style
{
struct Line
{
	Line(Point a, Point b) : m_a(a), m_b(b) {}

	double perimeter() {
		int x = abs(m_a.x - m_b.x);
		int y = abs(m_a.y - m_b.y);
		return sqrt(x*x + y*y);
	}

private:
	Point m_a;
	Point m_b;
};

struct Rectangle
{
	Rectangle(Point x, int w, int h) : m_x(x), m_w(w), m_h(h) {}
	Rectangle(Point a, Point b) : m_x(a), m_w(b.x - a.x), m_h(b.y - a.y) {}

	double perimeter() { return 2 * (m_w + m_h); }

private:
	Point m_x;
	int m_w;
	int m_h;
};

struct Circle
{
	Circle(Point x, int r) : m_x(x), m_r(r) {}

	double perimeter() { return 2 * m_r * M_PI; }

private:
	Point m_x;
	int m_r;
};



// Canvas that can hold: Line, Rectangle, Circle
struct Canvas {
	void addShape(const Line& x) { m_vL.push_back(x); }
	void addShape(const Rectangle& x) { m_vR.push_back(x); }
	void addShape(const Circle& x) { m_vC.push_back(x); }

	double totalPerimeter() {
		auto f = [](auto x){
			double s{0.0};
			for (auto& it : x)
				s += it.perimeter();
			return s;
		};
		return (f(m_vL) + f(m_vR) + f(m_vC));
	}

private:
	std::vector<Line> m_vL;
	std::vector<Rectangle> m_vR;
	std::vector<Circle> m_vC;
};

void populate(Canvas& canvas)
{
	std::mt19937 gen(k_randSeed);
	std::uniform_int_distribution<> shapeChoice(1, 3);
	std::uniform_int_distribution<> lc(1, 20);

	for (int i = 0; i < k_numOfShapes; ++i) {
		switch (shapeChoice(gen)) {
			case 1: {
				canvas.addShape(Line({lc(gen), lc(gen)}, {lc(gen), lc(gen)}));
			}
			break;
			case 2: {
				canvas.addShape(Rectangle({lc(gen), lc(gen)}, lc(gen), lc(gen)));
			}
			break;
			case 3: {
				canvas.addShape(Circle({lc(gen), lc(gen)}, lc(gen)));
			}
			break;
		}
	}
}

Canvas g_canvas;

double g_x;
}

static void dataVersion(benchmark::State& state) {
	data_style::populate(data_style::g_canvas);
	double x{0.0};
	// Code before the loop is not measured
	for (auto _ : state) {
		x += data_style::g_canvas.totalPerimeter();
	}
	data_style::g_x = x;
}
BENCHMARK(dataVersion);


//
//--------------------------------------------------------------
//


namespace tuple_style
{
struct Line
{
	Line(Point a, Point b) : m_a(a), m_b(b) {}

	double perimeter() {
		int x = abs(m_a.x - m_b.x);
		int y = abs(m_a.y - m_b.y);
		return sqrt(x*x + y*y);
	}

private:
	Point m_a;
	Point m_b;
};

struct Rectangle
{
	Rectangle(Point x, int w, int h) : m_x(x), m_w(w), m_h(h) {}

	Rectangle(Point a, Point b) : m_x(a), m_w(b.x - a.x), m_h(b.y - a.y) {}

	double perimeter() { return 2 * (m_w + m_h); }

private:
	Point m_x;
	int m_w;
	int m_h;
};

struct Circle
{
	Circle(Point x, int r) : m_x(x), m_r(r) {}

	double perimeter() { return 2 * m_r * M_PI; }

private:
	Point m_x;
	int m_r;
};


// Canvas that can hold: Line, Rectangle, Circle

template<typename... Ts>
struct Canvas {
	template<typename T>
	void addShape(const T& x) { std::get<std::vector<T>>(m_v).push_back(x); }

	double totalPerimeter() {
		auto f = [](auto x){
			double s{0.0};
			for (auto& it : x)
				s += it.perimeter();
			return s;
		};
		return (f(std::get<std::vector<Ts>>(m_v)) + ...);
	}

private:
	std::tuple<std::vector<Ts>...> m_v;
};

void populate(Canvas<Line, Rectangle, Circle>& canvas)
{
	std::mt19937 gen(k_randSeed);
	std::uniform_int_distribution<> shapeChoice(1, 3);
	std::uniform_int_distribution<> lc(1, 20);

	for (int i = 0; i < k_numOfShapes; ++i) {
		switch (shapeChoice(gen)) {
			case 1: {
				canvas.addShape(Line({lc(gen), lc(gen)}, {lc(gen), lc(gen)}));
			}
			break;
			case 2: {
				canvas.addShape(Rectangle({lc(gen), lc(gen)}, lc(gen), lc(gen)));
			}
			break;
			case 3: {
				canvas.addShape(Circle({lc(gen), lc(gen)}, lc(gen)));
			}
			break;
		}
	}
}

Canvas<Line, Rectangle, Circle> g_canvas;

double g_x;
}

static void tupleVersion(benchmark::State& state) {
	tuple_style::populate(tuple_style::g_canvas);
	double x{0.0};
	// Code before the loop is not measured
	for (auto _ : state) {
		x += tuple_style::g_canvas.totalPerimeter();
	}
	tuple_style::g_x = x;
}
BENCHMARK(tupleVersion);


//
//--------------------------------------------------------------
//