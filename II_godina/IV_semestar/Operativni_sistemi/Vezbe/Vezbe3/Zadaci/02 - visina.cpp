/* Napraviti konkurentni program sa 2 niti koje imaju isto telo niti. Svaka nit
 * najpre trazi od korisnika da unese svoju visinu. Nakon unosa, nit ispisuje
 * unetu vrednost na terminal.
 *
 * Sinhronizovati pristup terminalu kao deljenom resursu. Kada jedna nit stupi u
 * interakciju sa korisnikom, ne sme biti prekinuta dok se ne zavrsi kompletna
 * interakcija (i unos i ispis).
 */
#include <iostream>
#include <thread>
#include <mutex>

std::mutex m;

void f() {
    m.lock();
    std::cout << "Enter your height: ";
    std::string s;
    std::cin >> s;
    std::cout << s << std::endl;
    m.unlock();
}

int main() {
    int a = 0;
    std::thread t1(f);
    std::thread t2(f);
    t1.join(); t2.join();
    std::cout << a;
}
