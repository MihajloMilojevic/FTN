/*
Napraviti konkurentni program koji racuna srednju vrednost elemenata vektora. Racunanje srednje vrednosti se
vrsi tako sto se izracunaju parcijalne sume elemenata vektora koje se saberu u glavnoj niti i u istoj niti
se racuna srednja vrednost. Parcijalne sume prve 2 trecine vektora izracunaju 2 niti kreirane iz glavnog 
programa, dok parcijalnu sumu trece trecine vektora treba da izracuna nit main. OBEZBEDITI DA SE SVA TRI
RACUNA IZVRSAVAJU KONKURENTNO!

Nakon sto su izracunate sve 3 parcijalne sume, glavna nit treba da ih sabere i izracuna srednju vrednost 
svih elemenata vektora.

Broj elemenata vektora ne mora biti deljiv sa 3. Elementi vektora su tipa double.
*/


