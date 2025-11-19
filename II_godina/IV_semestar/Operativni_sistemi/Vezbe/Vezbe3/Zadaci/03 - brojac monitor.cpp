/* Napraviti konkurentni program koji modeluje klasu brojača.
 * Interfejs klase sadrži sledeće metode:
 *
 * class brojac {
 * public:
 *     void inc();
 *     void dec();
 *     friend ostream& operator<<(ostream& , brojac& );
 * };
 *
 * Metode inc i dec povećavaju, odnosno smanjuju vrednost brojača za 1. Operator
 * << služi za ispis brojača na ekran. Klasa mora biti thread-safe (da garantuje
 * ispravan rad i ako se objektu klase pristupa iz razlicitih niti).
 *
 * Kreirati jednu instancu date klase kojoj pristupaju 2 niti.
 *
 * Jedna nit poziva metodu uvećavanja brojača 1000000 puta, a druga metodu
 * smanjivanja brojača 1000000 puta.
 *
 * Na kraju programa ispisati konačnu vrednost brojača.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include <atomic>
#define ITER_COUNT 1000000

class brojac {
    
    private:
        std::atomic<int> c;
    public:
        brojac(): c(0) {}
        brojac(int x): c(x) {}
        void inc() {
            ++c;
        }
        void dec() {
            --c;
        }
        friend std::ostream& operator<<(std::ostream& out, brojac& b) {
            out << "brojac{" << b.c << "}";
            return out;
        }
};

brojac counter;

void inc() {
    for(int i = 0; i < ITER_COUNT; ++i) {
        counter.inc();
    }
}
void dec() {
    for(int i = 0; i < ITER_COUNT; ++i) {
        counter.dec();
    }
}

int main() {
    std::thread t1(inc);
    std::thread t2(dec);
    t1.join(); 
    t2.join();
    std::cout << counter;
}
