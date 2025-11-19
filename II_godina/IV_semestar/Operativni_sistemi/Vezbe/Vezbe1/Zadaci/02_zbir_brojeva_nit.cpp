/* Napraviti program koji kreira jednu nit kojoj se prosledjuju dva cela broja
 * a i b. U okviru niti sabrati brojeve i ispisati njihov zbir
 */
#include <iostream>
#include <string>
#include <thread>

void threadFunc(int a, int b) {
    std::cout << "Sum: " << a + b << std::endl;
}

int main() {
    int a, b;
    std::cout << "Enter first value: ";
    std::cin >> a;
    std::cout << "Enter second value: ";
    std::cin >> b;
    
    std::thread th1(threadFunc, a, b);
    th1.join();
}