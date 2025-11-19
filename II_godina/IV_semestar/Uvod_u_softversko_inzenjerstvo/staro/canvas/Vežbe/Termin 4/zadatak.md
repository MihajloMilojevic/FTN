# Zadatak

U ovom zadatku nastavljmo vježbanje od prethodnog časa.
Fokus ovog zadatka će biti paralelni rad nad istim repozitorijumom, PullRequest-ovi (PR) i rad sa granama.

## Priprema

1. Napraviti git repozitorijum u direktorijumu `my-machine`
2. Napraviti `.gitignore` fajl koji ignoriše sve `.png` fajlove i direktorijume `bin` i `obj`
3. Napraviti inicijalni commit koji commit-uje novokreirani `.gitignore`
4. Napraviti GitHub repozitorijum `git-practice`
5. Povezati lokalni repozitorijum koji se nalazi u `my-machine` i udaljeni repozitorijum `git-practice`
6. Poslati sve izmjene sa lokalnog repozitorijum-a na udaljeni repozitorijum
7. U roditeljskom direktorijumu od direktorijuma `my-machine` klonirati udaljeni repozitorijum
`git-practice` i smjestiti ga u direktorijum `not-my-machine`

## Sinhronizacija izmjena

Hajde da rezimiramo trenutno stanje:
- imamo udaljeni repozitorijum
- imamo dva lokalna repozitorijuma koja su oba povezana sa udaljenim repozitorijumom
- dva lokalna repozitorijuma nisu ista i nisu povezana (to možeš provjeriti tako što ćeš
da izmjeniš nešto u jednom i commit-uješ, ta izmjena i commit se neće nalaziti u drugom repozitorijumu)
Na ovaj način simuliramo istovremeni rad nad repozitorijumom (`git-practice`)
sa dva lokalna repozitorijuma koja će oba naizmjenično da prave izmjene i šalju ih i dobavljaju sa udaljenog repozitorijuma.
Na ovaj način vi radite u timu sa vašim kolegama, jedan član radi u `my-machine` (recimo da si to ti),
a drugi član radi u `not-my-machine` (recimo da je to tvoj kolega iz tima).
Možda ti ovaj pristup izgleda čudno, ali je vrlo zgodan da pomoću njega prođemo kroz
najčešće poteškoće i probleme u zajedničkom radu nad istim repozitorijumom.
Krenimo sa zagrijavanjem:

8. U repozitorijumu `my-machine` napravi iduće stanje repozitorijuma:
```
* 776483b (HEAD -> main) t1
* 249ba81 t0
```
9. Pošalji izmjene na udaljeni repozitorijum i trebalo bi da dobiješ iduće stanje:
```
* 776483b (HEAD -> main, origin/main) t1
* 249ba81 t0
```
10. Pređi u `not-my-machine` i povuci izmjene sa udaljenog repozitorijuma
11. Napravi iduće stanje repozitorijuma u `not-my-machine`:
```
* 21da622 (HEAD -> main) t2
* 776483b (origin/main, origin/HEAD) t1
* 249ba81 t0
```
12. Pošalji izmjene na udaljeni repozitorijum i trebalo bi da dobiješ iduće stanje:
```
* 21da622 (HEAD -> main, origin/main, origin/HEAD) t2
* 776483b t1
* 249ba81 t0
```

## Sinhronizacija izmjena u slučajevima kad udaljena grana ima nove commit-e koji ne postoje lokalno

Nakon zagrijavanja, hajde da vidimo šta se dešava ako ne koristimo grane i radimo nad istim repozitorijumom.
Ovdje ćemo simulirati situaciju kad je jedan kolega odradio neke izmjene i poslao ih na udaljeni repozitorijum,
pri tom je drugi kolega isto odradio neke izmjene i želi da ih pošalje (ali nakon što su izmjene prvog kolege već na udaljenom repozitorijumu).

13. U `not-my-machine` napravi iduće stanje:
```
* dd55854 (HEAD -> main, origin/main, origin/HEAD) t3
* 21da622 t2
* 776483b t1
* 249ba81 t0
```
14. Vrati se u `my-machine` i napravi iduće stanje:
```
* 69b5d9d (HEAD -> main) my-machine: t2
* 776483b (origin/main) t1
* 249ba81 t0
```
15. Probaj da pošalješ izmjene na udaljeni repozitorijum, i trebalo bi da dobiješ ovu poruku:
```
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:your-gh-username/git-practice'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Desila se iduća situacija:
```
* 69b5d9d (HEAD -> main) my-machine: t2
| * dd55854 (origin/main) t3
| * 21da622 t2
|/
* 776483b t1
* 249ba81 t0
```

Potrebno je da sinhronizujemo grane (dovučemo izmjene sa `origin/main` grane na našu granu, kako bi mogli završiti slanje izmjena na udaljeni repo).
Ovo ti je poznato od prethodnog časa, lokalni `main` (`69b5d9d`) se razlikuje od udaljenog `main`-a (`dd55854`).
Udaljeni main (`origin/main`) je specijalna grana, koja je read-only na koju ne možemo da commit-ujemo, ali možemo da je spojimo u našu granu.
`origin/main` je zapravo grana koja nam u lokalnom repozitorijumu govori i pokazuje gdje se main nalazi na udaljenom repozitorijumu (zato se zove remote tracking branch, jer samo prati udaljenu granu gdje se ona nalazi).
Pošto se grane razlikuju, nismo u mogućnosti da uradiom "fast-forward" i dobijemo sve izmjene sa udaljenog `main`-a.
Dakle potrebno je da uradimo `merge`. Uradićemo `merge` udaljenog `main`-a (`origin/main`) u lokalni `main`.

16. Jedna opcija jeste da uradite to manuelno sa:
`git merge origin/main`
A druga opcija jeste da kofigurišete `git pull` da svaki put kad se lokalna grana razlikuje od udaljene uradi merge udaljene grane u lokalnu.

Ako bi probali da uradimo `git pull` bez konfigurisanja, dobili bi ovu pourku:
```
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```
Možemo konfigurisati pull sa:
`git config pull.rebase false`

I onda možete da ponovite `git pull` koji će tad uraditi me merge izmjena.
Od ovog trenutka na dalje u ovom lokalnom repozitorijumu svaki idući pull će da uradi
i merge udaljenih izmjena u lokalne (ukoliko za tim ima potrebe).

Napomena: `git config pull.rebase true` je isto validna opcija, ali je malo naprednija jer `rebase` naredbu nismo radili na vježbama.
Ukoliko ste zainteresovani i želite da naučite i rebase, obratite se vašem predmetnom asistentu.

17. Pošaljite izmjene na udaljeni repozitorijum.

Na kraju treba da dobijete ovo stanje:
```
*   fe0c62c (HEAD -> maini, origin/main) Merge branch 'main' of github.com:your-gh-username/git-practice
|\
| * dd55854 t3
| * 21da622 t2
* | 69b5d9d my-machine: t2
|/
* 776483b t1
* 249ba81 t0
```

Ili ovo (ako ste uradili `git merge origin/main`):
```
*   fe0c62c (HEAD -> main, origin/main) Merge remote-tracking branch 'origin/main'
|\
| * dd55854 t3
| * 21da622 t2
* | 69b5d9d my-machine: t2
|/
* 776483b t1
* 249ba81 t0
```

Hajde da ponovimo sve još jednom.

18. Prebaci se u `not-my-machine` provjeri njegovo trenutno stanje i onda ga dovedi do idućeg stanja:
```
* ba9fbe6 (HEAD -> main) t4
* dd55854 (origin/main, origin/HEAD) t3
* 21da622 t2
* 776483b t1
* 249ba81 t0
```

19. Probaj da pošalješ izmjene na udaljeni repozitorijum. Na osnovu upustva iznad, pošalji izmjene na udaljeni repozitorijum.
```
*   7563e60 (HEAD -> main, origin/main, origin/HEAD) Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
|\
| *   f0c4652 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
| |\
| * | 69b5d9d my-machine: t2
* | | ba9fbe6 t4
| |/
|/|
* | dd55854 t3
* | 21da622 t2
|/
* 776483b t1
* 249ba81 t0
```

## Pull Request (PR)

20. U `my-machine` dovedi repozitorijum u iduće stanje:
```
* 7428146 (f1) t5
*   7563e60 (HEAD -> main, origin/main) Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
|\
| *   f0c4652 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
| |\
| * | 69b5d9d my-machine: t2
* | | ba9fbe6 t4
| |/
|/|
* | dd55854 t3
* | 21da622 t2
|/
* 776483b t1
* 249ba81 t0
```
21. Pošalji izmjene na udaljenu `f1` granu i napravi PR koji želi da spoji (`merge`-uje) `f1` u `main`.
22. Odobri i spoji PR
23. U `not-my-machine` dovuci sve izmjene. Trebalo bi da ti repozitorijum bude u ovom stanju:
```
*   d6abc84 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #1 from kzi-nastava/f1
|\
| * 7428146 t5
|/
*   7563e60 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
|\
| *   f0c4652 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
| |\
| * | 69b5d9d my-machine: t2
* | | ba9fbe6 t4
| |/
|/|
* | dd55854 t3
* | 21da622 t2
|/
* 776483b t1
* 249ba81 t0
```
24. U `not-my-machine` napravi iduće stanje repozitorijum-a:
```
* e0d8925 (HEAD -> f2, origin/f2) t6
*   d6abc84 (origin/main, origin/HEAD, main) Merge pull request #1 from kzi-nastava/f1
|\
| * 7428146 t5
|/
*   7563e60 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
|\
| *   f0c4652 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
| |\
| * | 69b5d9d my-machine: t2
* | | ba9fbe6 t4
| |/
|/|
* | dd55854 t3
* | 21da622 t2
|/
* 776483b t1
* 249ba81 t0
```
25. Napravi PR i spoji `f2` u `main`
26. Dovuci sve izmjene i u `my-machine` i u `not-my-machine`. Trebalo bi da dobiješ iduće stanje:
```
*   8c87aa2 (HEAD -> main, origin/main) Merge pull request #2 from kzi-nastava/f2
|\
| * e0d8925 t6
|/
*   d6abc84 Merge pull request #1 from kzi-nastava/f1
|\
| * 7428146 (origin/f1, f1) t5
|/
*   7563e60 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
|\
| *   f0c4652 Merge branch 'main' of github.com:kzi-nastava/vigilant-couscous
| |\
| * | 69b5d9d my-machine: t2
* | | ba9fbe6 t4
| |/
|/|
* | dd55854 t3
* | 21da622 t2
|/
* 776483b t1
* 249ba81 t0
```

## Konflikti i PR-ovi

27. U `my-machine` napravi fajl `foo` sa sadržajem `"asdf - 1"`, sve commit-uj na grani `f3`.
28. Napravi PR koji spaja `f3` u `main`.
29. U `not-my-machine` napravi fajl `foo` sa sadržajem `"000101010001011"`, commit-uj na grani `f4`.
30. Napravi PR koji spaja `f4` u `main`.

Prilikom kreiranja PR-a GitHub će te upozoriti da neće moći automatski da spoji tvoju granu `f4` u `main`, ali ćeš ipak moći napraviti PR.

Kako pristupiti riješavnju konflikta na PR-U? Isto kao i kod bilo kog konflikta.
Ovo je samo upozorenje, znači da se konflikt još nije desio.
Ono što treba da uradimo sad, jeste da izazovemo konflikt i riješimo ga.
To ćemo uraditi tako što ćemo lokalno da spojimo granu u koju želimo da spojimo našu `f4` granu (što je u ovom slučaju `main`).

1. U `not-my-machine` dovuci sve izmjene sa `main` i `f4` grana
2. Prebaci se na `f4` granu
2. Spoji (`merge`) `main` granu u `f4`
3. Riješi konflikt
4. Commit-uj riješen konflikt
5. Pošalji nove izmjene na `f4` grani
7. PR bi sad trebao da bude ažuriran i da je dugme za "Merge pull request" omogućeno i možete spojiti PR.

Dakle, pošto bi spajanje `f4` u `main` izazvalo konflikt, mi smo lokalno uradili obrnutu stvar - spojili `main` u `f4` i riješli konflikt.
Zašto smo lokalno odradili suprotnu stvar? Spajanje `f4` u `main` lokalno nema smisla, jer bismo time zaobišli PR i ne bi imalo potrebe za njim.
Spajanje `main` u `f4` takođe stvara konflikt (on se ni u čemu ne razlikuje od konflikta koji bi nastao spajanjem `f4` u `main`),
ali bitna razlika je da `main` ostaje netaknut i `f4` se ažurira tako da je kompatibilan sa `main`-om.

Provježbaj ovo još jednom:

31. Dovuci sve izmjene sa `main`-a i na `my-machine` i na `not-my-machine`
32. U `not-my-machine` napravi fajl `bar` sa sadržajem `"123456"`, commit-uj izmjene na grani `f5`.
33. Napravi PR koji spaja `f5` u `main`.
34. U  `my-machine` napravi fajl `bar` sa sadržajem `"arstgmneio"`, commit-uj izmjene na grani `f6`.
35. Napravi PR koji spaja `f6` u `main`.
36. Riješi konflikte lokalno po upustvu iznad i spoji PR.

## Kako izbjeći konflikte

Kako da smanjimo broj konflikata koji se dešavaju?

- prije nego što krenemo raditi, uvijek dovučemo sve izmjene sa udaljenog repozitorijuma
- svaki put radimo na novoj grani koju smo napravili od glavne grane

Probaj iduću tok i uoči razliku od prethodnog toka:

37. Dovuci sve izmjene sa `main`-a i na `my-machine` i na `not-my-machine`
38. U `not-my-machine` napravi fajl `baz` sa sadržajem `"987654"`, commit-uj izmjene na grani `f7`.
39. Napravi PR koji spaja `f7` u `main`.
40. U `my-machine` dovuci sve izmjene sa `main`-a.
41. U `my-machine` napravi fajl `baz` sa sadržajem `"arstgmneio"`, commit-uj izmjene na grani `f8`.
42. Napravi PR koji spaja `f9` u `main`.

Ukoliko smo samo dovukli sve izmjene (korak 40) prije nego što smo krenuli raditi, izbjegli smo konflikt!

## Preporučeni tok rada

1. Dovući izmjene sa udaljenog repozitorijuma
2. Napraviti svoju granu, od glavne grane, na kojoj ćete razvijati feature
3. Kad završite razvoj pošaljite izmjene i granu na udaljeni repozitorijum
4. Napravite PR koji spaja vašu granu u glavnu granu
5. Vratiti se na korak 1.
