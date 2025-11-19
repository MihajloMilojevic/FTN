/* Napraviti konkurentni program koji sadrzi main funkciju i 2 niti. Obe niti
 * pristupaju istoj celobrojnoj promenljivoj brojac, koja inicijalno ima
 * vrednost 0.
 * Prva nit 1000000 puta uvecava vrednost brojaca.
 * Druga nit isti broj puta smanjuje vrednost brojaca.
 *
 * Ukoliko je program ispravno napisan, na kraju programa vrednost brojaca mora
 * biti 0.
 */

#include <iostream>
#include <thread>
#include <mutex>

#define ITER_COUNT 1000000

std::mutex m;

void inc(int& x) {
    for(int i = 0; i < ITER_COUNT; ++i) {
        m.lock();
        ++x;
        m.unlock();
    }
}
void dec(int& x) {
    for(int i = 0; i < ITER_COUNT; ++i) {
        m.lock();
        --x;
        m.unlock();
    }
}

int main() {
    int a = 0;
    std::thread t1(inc, std::ref(a));
    std::thread t2(dec, std::ref(a));
    t1.join(); t2.join();
    std::cout << a;
}
