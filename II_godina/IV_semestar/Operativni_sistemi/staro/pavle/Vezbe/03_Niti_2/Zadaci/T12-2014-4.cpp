/*
Napraviti konkurentni program koji proverava stanja bankovnih racuna. Bankovni racuni su evidentirani u kontejeneru
kao par <kljuc, vrednost> pri cemu je kljuc broj racuna, a vrednost kolicina raspolozivih sredstava na tom racunu.
Raspoloziva sredstva su celobrojna vrednost dinara.

Provera bankovnih racuna se vrsi u okviru niti. Nit dobija 2 argumenta. Prvi argument je kontejner koji sadrzi 
<kljuc, vrednost> pri cemu kljuc predstavlja broj racuna koji treba proveriti, a vrednost predstavlja solventnost
datog racuna (tj. da li racun ima ili nema dovoljno sredstava). Drugi argument je kontejner prethodno opisanih 
bankovnih racuna uz pomoc kog nit treba da zakljuci koji su racuni od navedenih u prvom kontejneru solventni a 
koji nisu i da to zabeleze u okviru prvog kontejnera.

Minimalna kolicina novca za solventnost je 5000 dinara. Napraviti 5 bankovnih racuna sa proizvoljnom kolicinom
novca na njima i u okviru niti proveriti proizvoljna 3 racuna od tih 5. Na kraju u glavnom programu ispisati 
stanje solventnosti svakog od ta 3 racuna. 

Predpostavlja se da korisnik trazi stanje samo postojecih racuna tj. ne trazi stanje racuna koji ne postoji u bazi.
Ispis bi trebao da izgleda ovako:

    Racun br: 0 je SOLVENTAN
    Racun br: 1 je NESOLVENTAN
    Racun br: 3 je SOLVENTAN
    
U programu postoji samo jedna nit koja vrsi proveru solventnosti.    
*/


