/* Napraviti sekvencijalni program koji izračunava sumu svih elemenata vektora
 * sekvencijalno, koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
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
   double sum;
   f(v.cbegin(), v.cend(), sum);
   std::cout << "Sum: " << sum << std::endl;
}