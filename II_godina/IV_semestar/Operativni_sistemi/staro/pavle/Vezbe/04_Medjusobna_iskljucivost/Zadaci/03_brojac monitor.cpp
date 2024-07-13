/*		
Napraviti konkurentni program koji modeluje klasu brojača. 
Interfejs klase sadrži sledeće metode: 

class brojac {
   public:
      void inc();
      void dec();
      friend ostream& operator<<(ostream& , brojac& );
};

Metode inc i dec povećavaju, odnosno smanjuju vrednost brojača za 1. 
Operator << služi za ispis brojača na ekran.
Klasa mora biti thread-safe (da garantuje ispravan rad i ako se objektu klase pristupa iz
razlicitih niti).

Kreirati jednu instancu date klase kojoj pristupaju 2 niti.

Jedna nit poziva metodu uvećavanja brojača 1000000 puta, 
a druga metodu smanjivanja brojača 1000000 puta. 

Na kraju programa ispisati konačnu vrednost brojača.
*/
