insert into kupac (idkup, nazkup, mestkup) values (1, 'NS Gradnja', 'Novi Sad');
insert into kupac (idkup, nazkup, mestkup) values (2, 'BG-Stan', 'Beograd');
insert into kupac (idkup, nazkup, mestkup) values (3, 'Nis-Invest', 'Nis');
insert into kupac (idkup, nazkup, mestkup) values (4, 'Buducnost', 'Novi Sad');

insert into artikal (idart, nazart, jcena) values (1, 'Cement', 400);
insert into artikal (idart, nazart, jcena) values (2, 'Pesak', 500);
insert into artikal (idart, nazart, jcena) values (3, 'Blok', 20);
insert into artikal (idart, nazart, jcena) values (4, 'Cigla', 10);
insert into artikal (idart, nazart, jcena) values (5, 'Crep', 50);

insert into faktura (brfak, datum, idkup) values (1, DATE '2010-01-10', 1);
insert into faktura (brfak, datum, idkup) values (2, DATE '2010-02-04', 3);
insert into faktura (brfak, datum, idkup) values (3, DATE '2009-05-03', 2);
insert into faktura (brfak, datum, idkup) values (4, DATE '2010-06-11', 1);
insert into faktura (brfak, datum, idkup) values (5, DATE '2009-08-09', 2);

insert into stavka (brfak, rbrst, idart, kol, cena) values (4, 1, 3, 500, 10000);
insert into stavka (brfak, rbrst, idart, kol, cena) values (1, 2, 2, 15, 7500);
insert into stavka (brfak, rbrst, idart, kol, cena) values (4, 3, 1, 20, 8000);
insert into stavka (brfak, rbrst, idart, kol, cena) values (1, 1, 3, 125, 2500);
insert into stavka (brfak, rbrst, idart, kol, cena) values (5, 2, 4, 2000, 20000);
insert into stavka (brfak, rbrst, idart, kol, cena) values (2, 1, 1, 40, 16000);
insert into stavka (brfak, rbrst, idart, kol, cena) values (5, 1, 1, 50, 20000);
insert into stavka (brfak, rbrst, idart, kol, cena) values (4, 2, 4, 900, 9000);
insert into stavka (brfak, rbrst, idart, kol, cena) values (3, 1, 2, 6, 3000);