/* Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na N delova tako svaka nit sabira duzina vektora/broj
 * niti elemenata vektora.
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
    int N = 5;
    std::vector<std::thread> threads(N);
    int d = v.size() / N;
    std::vector<double> parts(N, 0.0);
    for(int i = 0; i < N; ++i) {
        if (i < N - 1) 
            threads[i] = std::thread(f, v.cbegin() + i * d, v.cbegin() + (i+1)*d, std::ref(parts[i]));
        else
            threads[i] = std::thread(f, v.cbegin() + i * d, v.cend(), std::ref(parts[i]));
    }
    for(int i = 0; i < N; ++i) {
        threads[i].join();
    }
    f(parts.cbegin(), parts.cend(), sum);
    std::cout << "Sum: " << sum << std::endl;
}