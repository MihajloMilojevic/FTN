#include <iostream>
#include <vector>
#include <list>

template<typename T>
class Box {
private:
    T elem;
public:
    Box(): elem() {}
    Box(T el): elem(el) {}
    T get() { return elem; }
    void set(T value) { elem = value; }
};

template<typename T>
T minValue(const T& a, const T& b) {
    return a <= b ? a : b;
}

int main()
{
    std::cout << minValue(4, 5) << std::endl;
    std::cout << minValue(2.3, 4.5) << std::endl;
    std::cout << minValue(7.3f, 5.2f) << std::endl;
    std::cout << minValue('c', 'm') << std::endl;

    std::vector<int> vint;
    for (int i = 1; i <= 10; ++i) vint.push_back(i);
    for (int i = 0; i < vint.size(); ++i) std::cout << vint.at(i) << " ";
    std::cout << "\n";
    vint.insert(vint.begin(), 11);
    vint.pop_back();
    for (int i = 0; i < vint.size(); ++i) std::cout << vint.at(i) << " ";
    std::cout << "\n";

    if (!vint.empty()) vint.clear();
    for (int i = 0; i < vint.size(); ++i) std::cout << vint.at(i) << " ";
    std::cout << "\n";

    std::list<int> lint;
    for (int i = 1; i <= 10; ++i) lint.push_back(i);
    //lint.reverse();
    for (auto it = lint.rbegin(); it != lint.rend(); ++it) 
        std::cout << *it << " ";
    std::cout << "\n";

    lint.push_front(0);
    lint.push_back(11);

    for (auto it = lint.begin(); it != lint.end(); ++it)
        std::cout << *it << " ";
    std::cout << "\n";

    auto it = lint.begin();
    advance(it, 3);

    lint.insert(it, 4);
    lint.insert(it, 5);
    lint.insert(it, 6);

    for (auto it = lint.begin(); it != lint.end(); ++it)
        std::cout << *it << " ";
    std::cout << "\n";

    lint.sort();

    for (auto it = lint.begin(); it != lint.end(); ++it)
        std::cout << *it << " ";
    std::cout << "\n";

    lint.unique();

    for (auto it = lint.begin(); it != lint.end(); ++it)
        std::cout << *it << " ";
    std::cout << "\n";
}
