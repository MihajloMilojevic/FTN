/* Napraviti konkurentni program koji simulira serijalizaciju objekata u JSON
 * format pri slanju podataka sa veb servera na klijent. JSON objekti se sastoje
 * od parova <kljuc,vrednost>.
 *
 * U main funkciji, koriscenjem odgovarajuceg STL kontejnera, definisati JSON
 * objekat Korisnik koji ima sledece parove:
 *
 *     <id,1>
 *     <ime,Marko>
 *     <prezime,Markovic>
 *     <email,marko.markovic@gmail.com>
 *
 * Zatim napraviti posebnu nit koja ispisuje sadrzaj JSON objekta u JSON
 * formatu.
 *
 * Ispis u JSON formatu izgleda ovako:
 *
 *     {"email":"marko.markovic@gmail.com","id":"1","ime":"Marko","prezime":"Markovic"}
 *
 * Pri ispisu nije vazan redosled parova.
 */
#include <iostream>
#include <thread>
#include <map>

void f(const std::map<std::string, std::string>& obj) {
    std::cout << "{";
    auto it = obj.cbegin();
    std::cout << "\"" << it->first << "\": \"" << it->second << "\"";
    ++it;
    for(; it != obj.cend(); ++it) {
        std::cout << ",\"" << it->first << "\": \"" << it->second << "\"";
    } 
    std::cout << "}";
}

int main() {
    std::map<std::string, std::string> obj{
        {"id", "SV57/2023"}, 
        {"ime", "Mihajlo"},
        {"prezime", "Milojevic"},
        {"email", "milojevicm374@gmail.com"}
    };
    std::thread t(f, obj);
    t.join();
}