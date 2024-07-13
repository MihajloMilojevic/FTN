/*
Napraviti konkurentni program za izracunavanje obima kruznica.
Na pocetku programa korisnik unosi koliko niti treba da se kreira.
Svaka nit u svom telu odredjuje poluprecnik kruznice kao
pseudoslucajan broj izmedju 1 i 10.
Za dobijanje pseudoslucajnog broja izmedju 1 i 10, pozvati
rand()%10 + 1

Na osnovu generisanog poluprecnika, nit izracunava obim kruznice i
u STL kontejner ubacuje redni broj niti i obim kruznice.
Za broj PI, koristiti konstantu M_PI iz zaglavlja <cmath>

Na kraju glavnog programa, potrebno je ispisati koja nit je generisala najveci obim kruznice.
Primer ispisa:
Najvecu kruznicu u obimu 50.2655 iscrtala je nit broj 3.

*/