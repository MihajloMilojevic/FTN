/* Napraviti konkurentni program koji radi formiranje evidencije studenata.
 * Studentska sluzba (glavni program) salje 2 kontejnera niti koja formira
 * evidenciju. Prvi kontejner sadrzi indekse studenata, dok drugi kontejner
 * sadrzi ime i prezime studenta (kao jedan element kontejnera). Podrazumeva se
 * da indeks na i-toj poziciji prvog kontejnera odgovara imenu i prezimenu na
 * i-toj poziciji drugog kontejnera.
 *
 * Zadatak niti je da formira novi kontejner koji sadrzi parove
 * <kljuc, vrednost> uz pomoc prethodno opisanih kontenjera brojeva indeksa
 * (kljuc) i imena sa prezimenima (vrednost).
 *
 * Nakon zavrsetka rada niti u glavnom programu ispisati sadrzaj novoformiranog
 * kontejnera sa parovima <kljuc, vrednost>.
 *
 * Ispis bi trebao da izgleda ovako:
 *
 *     Indeks: RA 111/2012 Ime i prezime: Petar Petrovic
 *     Indeks: RA 222/2012 Ime i prezime: Stefan Stefanovic
 *     Indeks: RA 333/2012 Ime i prezime: Milica Micic
 *
 * U programu postoji samo jedna nit koja kreira evidenciju studenata.
 */
