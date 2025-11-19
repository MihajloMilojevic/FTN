# Upustvo

Rekreirati dati git graph.
Pored grafa dato je upustvo koje može služiti kao vodič do rješenja.
Obješnjenje sintakse koja je korišćena u upustvu:
`t0) foo > 0` znači u `t0` (što može biti commit, ali ne u svim slučajevima) fajl `foo` ima sadržaj `0`
Moguće je specificirati i granu na kojoj treba da se izvrši izmjena, npr:
`t1) f1 : foo > 1` znači da u `t1` na grani `f1` fajl `foo` ima sadržaj `0`
Ukoliko grana nije navedena, podrazumjeva se da je izmjena odrađena na podrazumjevanoj (glavnoj, engl. default) grani (obično je to main ili master).
Prema tome u primjeru iznad za `t0` izmjena je odrađena na glavnoj grani.
Pored izmjene, upustvo sadrži i informacije o merge događajima, npr:
`t2) merge f1` znači da se u glavnu granu merge-uje grana `f1`.
(napomena: pošto merge ne proizvede novi komit u svim slučajevima (kad se desi fast-forward) `tN` u tim slučejvima ne označava commit, već samu merge naredbu).

hint: bilo koji commit u grafu koji ima dva roditelja (dvije strelice izlaze iz njega do drugih commit-a) jeste merge commit.
hint: moguće je u terminalu provjeriti trenutno stanje git grafa sa:
`git log --graph --oneline`
extra hint: moguće je napraviti alias za brže kucanje
`git config --global alias.graph "log --oneline --graph --decorate --all"`
i onda se koristi `git graph` umjesto prethodne naredbe.

## Zadatak 1

```
* caff469 (HEAD -> main, f1) t1
* 04e58e0 t0
```

t0) foo > 0
t1) f1 : foo > 1
t2) merge f1

## Zadatak 2

```
*   461bf72 (HEAD -> main) t3
|\
| * 4f7fdb4 (f1) t2
* | 6573a0c t1
|/
* 406cec5 t0
```

t0) foo > 0
t1) bar > 1
t2) f1 : foo > 1
t3) merge f1

## Zadatak 3

```
*   461bf72 (HEAD -> main) t4
|\
| * 4f7fdb4 (f1) t2
* | 6573a0c t1
|/
* 406cec5 t0
```

t0) foo > 0
t1) foo > 1
t2) f1 : foo > 42
t3) merge f1

## Zadatak 4

```
*   469600f (HEAD -> main) t6
|\
| * 91cd815 (f2) t5
| * bdad88e t3
* |   1622ff7 t4
|\ \
| * | d4a978c (f1) t2
| |/
* / a7c9dbb t1
|/
* 5df919d t0
```

t0) foo > 0
t1) baz > 1
t2) f1 : foo > 11
t3) f2 : baz > 33
t4) merge f1
t5) f2 : foo > 22
t6) merge f2

## Zadatak 5

```
*   672abc7 (HEAD -> main, f1) t10
|\
| *   3a56e0f (f2) t8
| |\
| * | 8e43858 t6
| * |   d41ca34 t5
| |\ \
| * | | 9fc1178 t3
* | | |   3463804 (f3) t7
|\ \ \ \
| |_|/ /
|/| | /
| | |/
| |/|
| * | 8dc16f4 t2
* | | 44a3151 t4
|/ /
* / b8c9a92 t1
|/
* eb503a0 t0
```

upustvo za konvenciju ispod: f2(t0) - znači da se grana f2 napravila sa početnim commit-om t0.

t0) foo > 1
t1) f1 : foo > 2
t2) f1 : baz > 32
t3) f2(t0) : foo > 3
t4) f3(t1) : foo > 4
t5) f2 merge f3
t6) f2 : baz > 7
t7) f3 merge f1
t8) f2 merge f1
t9) f1 merge f3
t10) f1 merge f2
t11) main merge f1

## Zadatak 6

```
* c6f119e (HEAD -> main, f1) t14
*   83ae7fe t13
|\
| * 6dd4575 (f3) t12
| *   f6dc07e t10
| |\
| * | c708784 t4
| * | d19c11b t3
* | |   8587930 t11
|\ \ \
| | |/
| |/|
| * | 6879471 (f2) t8
| * |   20763db t6
| |\ \
| * | | 4fef899 t2
* | | | fdf9dcd t7
| |/ /
|/| |
* | | 767d3ce t5
|/ /
* / 1956be3 t1
|/
* cffbfab t0
```

t0) foo > 0
t1) f1 : foo > 2
t2) f2 : foo > 3
t3) f3(t0) : foo > 4
t4) f3 : bar > 1
t5) f1 : bar > 2
t6) f2 merge f1
t7) f1 : baz > 1
t8) f2 : baz > 2
t9) main merge f3
t10) f3 merge f2
t11) f1 merge f2
t12) f3 : baz > 34
t13) f1 merge f3
t14) f1 : baz > 42
t15) main merge f1

