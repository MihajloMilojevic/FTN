/*
Napraviti konkurentni program koji simulira serijalizaciju objekata u JSON format
pri slanju podataka sa veb servera na klijent.
JSON objekti se sastoje od parova <kljuc,vrednost>.

U main funkciji, koriscenjem odgovarajuceg STL kontejnera, definisati JSON objekat Korisnik koji ima sledece parove:
<id,1>
<ime,Marko>
<prezime,Markovic>
<email,marko.markovic@gmail.com>

Zatim napraviti posebnu nit koja ispisuje sadrzaj JSON objekta u JSON formatu.
Ispis u JSON formatu izgleda ovako:
{"email":"marko.markovic@gmail.com","id":"1","ime":"Marko","prezime":"Markovic"}

Pri ispisu nije vazan redosled parova.

*/