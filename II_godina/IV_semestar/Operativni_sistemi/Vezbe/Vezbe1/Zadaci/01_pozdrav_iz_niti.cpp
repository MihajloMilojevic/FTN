/* Napraviti program koji kreira jednu nit i u okviru nje ispisuje proizvoljnu
 * recenicu.
 */
#include <iostream>
#include <string>
#include <thread>

void threadFunc(std::string s) {
    std::cout << s << std::endl;
}

int main() {
    std::string s;
    std::getline(std::cin, s);
    std::thread th1(threadFunc, s);
    th1.join();
}