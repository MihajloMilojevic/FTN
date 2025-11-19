/* Napisati konkurentni program koji stvara jednu nit.
 * Nit od glavnog programa kao parametar dobija ceo broj i ima zadatak da uveca
 * vrednost broja za 1.
 *
 * Ispisati vrednost broja nakon zavrsetka rada niti
 */
#include <iostream>
#include <string>
#include <thread>

void threadFunc(int& x) {
    ++x;
}

int main() {
    int x = 0;
    std::cout << "Before: " << x << std::endl;
    std::thread th1(threadFunc, std::ref(x));
    th1.join();
    std::cout << "After: " << x << std::endl;
}