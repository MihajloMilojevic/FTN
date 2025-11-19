/* Napraviti konkurentni program  (koristeći funkciju f()) koji sabira
 * korespodentne elemente kontejnera  a i b, a rezultat smešta u vektor zbir.
 *
 * Dato je telo niti:
 *
 * void f(ci a_begin, ci a_end, ci b_begin, vector<double>::iterator sum_begin);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Program optimizovati za procesor sa 2 jezgra.
 *
 * Napomene: Podrazumeva se da su kontejneri a i b iste dužine.
 */
#include <iostream>
#include <string>
#include <vector>
#include <thread>

typedef std::vector<double>::const_iterator ci;

void f(ci a_begin, ci a_end, ci b_begin, std::vector<double>::iterator sum_begin) {
    while(a_begin != a_end) {
        *sum_begin = *a_begin + *b_begin;
        ++a_begin; ++b_begin; ++sum_begin;
    }
}

std::ostream& operator<<(std::ostream& out, std::vector<double>& v) {
    for(const auto e : v) {
        out << e << " ";
    }
    return out;
}

int main() {
   std::vector<double> a{1, 2, 3, 4, 5, 6, 7, 8, 9};
   std::vector<double> b{9, 8, 7, 6, 5, 4, 3, 2, 1};
   std::vector<double> sum(a.size());
   int d = a.size() / 2;
   std::thread t1(f, a.cbegin(), a.cbegin() + d, b.cbegin() + d, sum.begin() + d);
   std::thread t2(f, a.cbegin(), a.cend(), b.cbegin(), sum.begin());
   t1.join(); t2.join();
   std::cout << "Sum: " << sum << std::endl;
}