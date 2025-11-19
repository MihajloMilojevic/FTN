/* Napraviti konkurentni program koji kreira 5 niti od kojih svaka izvrsava isti
 * kod (svaka nit ima isto telo niti).
 * Svaka nit dobija svoj redni broj prilikom kreiranja.
 * U telu niti svaka nit treba da ispise svoj redni broj.
 */
#include <iostream>
#include <string>
#include <thread>

#define THREAD_COUNT 5

void threadFunc(int i) {
    std::cout << i << std::endl;
}

int main() {
    std::thread threads[THREAD_COUNT];
    for(int i = 0; i < THREAD_COUNT; ++i) {
        threads[i] = std::thread(threadFunc, i);
    }
    for(int i = 0; i < THREAD_COUNT; ++i) {
        threads[i].join();
    }
}