/* Napraviti konkurentni program za simulaciju logovanja na udaljeni racunar.
 *
 * Da bi se logovao, u glavnom programu korisnik redom treba da unese:
 *
 *     login <enter>
 *     <korisnicko_ime> <enter>
 *     <lozinka> <enter>
 *
 * Nakon toga posebna nit treba da utvrdi da li korisnik moze da se uloguje.
 *
 * Provera ispravnosti logovanja vrsi se na osnovu evidencije korisnika. U
 * glavnom programu, koriscenjem STL kontejnera, evidentirati sledece korisnike:
 *
 *     1. korisnicko_ime: milan, lozinka: 12345
 *     2. korisnicko_ime: marko, lozinka: xyz
 *     3. korisnicko_ime: admin, lozinka: 4dm1n
 *
 * Nit treba da utvrdi da li je najpre unesena rec "login". Ako jeste, korisnik
 * se moze ulogovati ako postoji evidentiran korisnik sa unesenim  korisnickim
 * imenom i lozinkom.
 *
 * Ako je logovanje uspesno, nit ispisuje:
 *
 *     Korisnik uspesno prijavljen.
 *
 * U slucaju neuspesnog logovanja, nit ispisuje:
 *
 *     Neuspesna prijava!
 */
