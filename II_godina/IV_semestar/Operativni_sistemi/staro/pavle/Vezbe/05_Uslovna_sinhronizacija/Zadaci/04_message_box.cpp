/*
	Data je klasa Message_box koja predstavlja sanduce za poruke bilo kojeg tipa.
	Message_box sadrzi dve metode:
        send(const MESSAGE* message) - za ubacivanje poruke u sanduce i
        receive() - za preuzimanje poruke iz sanduceta

	Date su niti proizvodjac i potrosac.
	Nit proizvodjac ubacuje tri poruke u sanduce, a nit potrosac ih preuzima i ispisuje.
	   
	Prepraviti klasu tako da bude implementirana u skladu sa sledecim pravilima:
		
		- Nit proizvodjac ne sme da upi�e novu poruku, dok nit potrosac ne preuzme prethodno upisan polo�aj.
		- Nit potrosac ne sme da preuzme polo�aj kursora pre nego �to ga nit proizvodjac upi�e.
		- Nit potrosac ne sme dva puta da preuzme isti polo�aj kursora.

		(Ili kori�cenjem stanja: 
			Nit proizvodjac ne sme da pi�e u punu deljenu promenljivu.
			Nit potrosac ne sme da cita iz prazne deljene promenljive.)
		
     Ako program ispravno radi, sve tri poruke trebaju biti preuzete i ispisane, tako da ispis bude:
	2
	9
	7
*/

#include <thread>
#include <iostream>

using namespace std;

template<class MESSAGE>
class Message_box {
    MESSAGE content;
  public:
    void send(const MESSAGE* message);
    MESSAGE receive();
};

template<class MESSAGE>
void Message_box<MESSAGE>::send(const MESSAGE* message)
{
    content = *message;
}

template<class MESSAGE>
MESSAGE Message_box<MESSAGE>::receive()
{
    return content;
}

void proizvodjac(Message_box<int>& mb) {
    int a = 2;
    mb.send(&a);
    a = 9;
    mb.send(&a);
    a = 7;
    mb.send(&a);
}

void potrosac(Message_box<int>& mb) {
    cout << "Preuzeto: " << mb.receive() << endl;
    cout << "Preuzeto: " << mb.receive() << endl;
    cout << "Preuzeto: " << mb.receive() << endl;
}

int main() {
    Message_box<int> mb;

    thread t1(proizvodjac, ref(mb));
    thread t2(potrosac, ref(mb));

    t1.join();
    t2.join();
}