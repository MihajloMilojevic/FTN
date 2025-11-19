/* Napraviti konkurentni program koji pita korisnika koliko niti da stvori, a
 * zatim stvara zadati broj niti. Pri instanciranju nit dobija redni broj pod
 * kojim je stvorena. Svaka nit ispisuje svoj redni broj i svoj identifikator.
 */
#include <iostream>
#include <thread>
#include <vector>

void f(int num) {
    std::cout << "Order number: " << num << " Id: " << std::this_thread::get_id() << std::endl;
}

int main() {
    int N;
    std::cout << "Enter the number of threads: ";
    std::cin >> N;
    std::vector<std::thread> threads(N);
    for(int i = 0; i < N; ++i) threads[i] = std::thread(f, i);
    for(int i = 0; i < N; ++i) threads[i].join();
}