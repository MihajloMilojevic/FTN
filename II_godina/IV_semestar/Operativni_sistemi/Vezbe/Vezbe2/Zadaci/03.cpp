/* Napraviti konkurentni program koji stvara jednu nit. Nit ima 2 parametra.
 * Jedan je referenca na ulaznu listu a drugi referenca na izlaznu. Nit treba da
 * elemente ulazne liste prebaci u izlaznu tako da stoje u obrnutom redosledu.
 * Ispisati izgled izlazne liste nakon rada niti.
 */
#include <iostream>
#include <thread>
#include <list>

template<class T>
std::ostream& operator<<(std::ostream& out, const std::list<T> l) {
    for (const auto e : l) out << e << " ";
    return out;
}

void f(std::list<int>& a, std::list<int>& b) {
    b.clear();
    for(auto it = a.cbegin(); it != a.cend(); ++it) 
        b.insert(b.begin(), *it);
}

int main() {
    std::list<int> a{1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::list<int> b(a);

    std::cout << "Before:\nA: " << a << "\nB: " << b << std::endl;
    std::thread t(f, std::ref(a), std::ref(b));
    t.join();
    std::cout << "After:\nA: " << a << "\nB: " << b << std::endl;
}