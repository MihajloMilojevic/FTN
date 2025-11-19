/* Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na 2 dela tako da prvu polovinu vektora sumira prva
 * nit, a drugu polovinu druga nit.
 *
 * Napomena: ovakva optimizacija sumiranja je znacajna kada se radi na
 * dvojezgarnom procesoru za vektore velike duzine.
 */
#include <iostream>
#include <string>
#include <vector>
#include <thread>

typedef std::vector<double>::const_iterator ci;

void f(ci begin, ci end, double& sum) {
    while(begin != end) {
        sum += *begin;
        ++begin;
    }
}

int main() {
   std::vector<double> v{1, 2, 3, 4, 5, 6, 7, 8, 9};
   double sum = 0;
   double left = 0, right = 0;
   std::thread t1(f, v.cbegin(), v.cbegin() + v.size()/2, std::ref(left));
   std::thread t2(f, v.cbegin() + v.size()/2, v.cend(), std::ref(right));
   t1.join(); t2.join();
   sum = left + right;

   std::cout << "Left: " << left << std::endl;
   std::cout << "Right: " << right << std::endl;
   std::cout << "Sum: " << sum << std::endl;
}