/* Naparviti klasu mb (message_box) koja sadrzi n komunikacionih kanala. (n se
 * odredjuje u trenutku instanciranja objekta klase). Komunikacioni kanal
 * (sanduce) omogucava komunikaciju izmedju proizvodjaca i potrosaca nazavisnu
 * od ostalih komunikacija. Svaki kanal moze da sadrzi neogranicen broj poruka.
 *
 * mb ima dve operacije.
 * 1. mb::send() je neblokirajuca operacija sa dva parametra:
 *  - vrednosti (objekt) koja se salje i
 *  - indeksom kanala u koji se salje.
 *
 * 2. mb::receive() je blokirajuca operacija koja prihvata indeks kanala iz 
 *  kojeg ocekuje poruku, a vraca objekt poruke.
 *
 * Jednu poruku je moguce preuzeti samo jednom (pri preuzimanju, poruka se i
 * izbacuje iz sanduceta). Ako u kanalu nema poruke, nit koja je pozvala
 * receive() ceka poruku. Niti koje pozovu receive moraju da dobiju poruke iz
 * odgovarajuceg kanala, ali ne moraju da dobiju poruke u redosledu u kojem su
 * one (poruke) poslate.
 *
 * Operacije send() i receive() bacaju izuzetak ako im se prosledi kanal koji ne
 * postoji.
 *
 * Operacije ove klase su thread safe.
 */

template<typename T, int N>
class mb {
public:
   mb();
   ~mb();
   void send(T data, int channel);
   T receive(int channel);
};

mb<char, 3> mb3;

//proizvodjac salje tri uzastopna karaktera pocevsi od prosledjenog karaktera c
void producer(char c, int channel) {
   this_thread::sleep_for(chrono::seconds(1));
   mb3.send(c, channel);
   this_thread::sleep_for(chrono::seconds(1));
   mb3.send(c+1, channel);
   this_thread::sleep_for(chrono::seconds(1));
   mb3.send(c+2, channel);
}

void consumer(int channel) {
   static mutex mx;
//   this_thread::sleep_for(chrono::seconds(1));
   char c = mb3.receive(channel);
   unique_lock<mutex> l(mx);
   cout << "[" << channel << "]= " << c << endl;
}

const int PROD=3;
const int CONS=9;

int main() {
   thread prod[PROD];
   thread cons[CONS];

   //posto svaki proizvodjac posalje tri uzastopna karaktera
   //pocevsi od prosledjenog, znaci da pri ispisu preuzeti karakteri
   //treba da budu (u proizvoljnom redosledu):
   //a,b,c, g,h,i, m,n,o
   char poruke[] = {'a', 'g', 'm'};

   for(int i=0;i<PROD;++i)
      prod[i]=thread(producer, poruke[i], i%3);
   for(int i=0;i<CONS;++i)
      cons[i]=thread(consumer, i%3);
   for(int i=0;i<PROD;++i)
      prod[i].join();
   for(int i=0;i<CONS;++i)
      cons[i].join();

   return 0;
}