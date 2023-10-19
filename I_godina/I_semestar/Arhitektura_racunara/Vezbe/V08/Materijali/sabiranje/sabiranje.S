# Program za sabiranje dva broja u proizvoljnoj bazi
# Imenko Prezimić ra1234

# Napisati asemblerski program koji, koristeći potprograme za konverziju
# za bilo koju bazu 2‑36, vrši sabiranje dva neoznačena cela broja data u
# znakovnom obliku i rezultat vraća u znakovnom obliku. Sve konverzije
# raditi odmah nakon unosa, a u slučaju greške prekinuti dalji rad
# programa i ispisati odgovarajuću poruku. Primer korišćenja:
#       Unesite bazu broja:16
#       Unesite broj:Fa
#       Unesite bazu broja:8
#       Unesite broj:123
#       Unesite bazu rezultata:2
#       Rezultat:101001101
# Za ostale primere pokrenuti testiraj.sh.
# Dodatni primeri se mogu napraviti pomoću kalkulatora (Accessories/Calculator)

ulaz1:      .ascii "Unesite bazu broja:\0"
ulaz2:      .ascii "Unesite broj:\0"
ulaz3:      .ascii "Unesite bazu rezultata:\0"
izlaz1:     .ascii "Rezultat:\0"
greska1:    .ascii "Greska: pogresan znak!\0"
greska2:    .ascii "Greska: prekoracenje!\0"

