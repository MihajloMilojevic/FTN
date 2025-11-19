/* Sabrati korespodentne elemente vektora a i b, a zbirove smestiti na
 * odgovarajuce pozicije vektora c. Obezbediti da svako sabiranje obavlja
 * posebna nit.
 */
#include <iostream>
#include <string>
#include <vector>
#include <thread>

typedef std::vector<double>::iterator vdi;
typedef std::vector<double>::const_iterator vdci;


void f(vdci a, vdci b, vdi c) {
    *c = *a + *b;
}

std::ostream& operator<<(std::ostream& out, const std::vector<double>& v) {
    for(const auto e : v) out << e << " ";
    return out;
}

int main() {
    std::vector<double> a{1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<double> b{2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::vector<double> c(a.size());
    std::vector<std::thread> threads(a.size());
    for(int i = 0; i < a.size(); ++i) threads[i] = std::thread(f, a.cbegin()+i, b.cbegin()+i, c.begin() + i);
    for(int i = 0; i < a.size(); ++i) threads[i].join();
    std::cout << c << std::endl;
}