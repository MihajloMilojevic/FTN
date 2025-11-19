/* Napisati program koji proverava koje se od zadatih tacaka nalaze u/na 
 * kruznici, a koje su van kruznice.
 * Tacke se nalaze u vektoru points:
 * 
 * struct Point { double x, y; };
 * vector<Point> points;
 * 
 * Definisati klasu:
 * 
 * class Circle {
 *   ...
 * public:
 *   Circle(const Point& t, const double r_);
 *   void check(const vector<Point> p, vector<bool>& belong);
 * };
 * 
 * Objekt tipa Circle, za svaku tacku iz vektora, izracunava da li se ona nalazi:
 *     - u krugu (ili na kruznici)
 *         + korespodentni element vektora belong dobija vrednost true ili
 *     - van kruga
 *         + korespodentni element vektora belong dobija vrednost false.
 * 
 * Stvoriti nit koja poziva funkciju check nad objektom klase Circle.
 */
