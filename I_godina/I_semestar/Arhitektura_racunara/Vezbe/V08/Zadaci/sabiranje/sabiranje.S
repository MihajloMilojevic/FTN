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
.section .data
ulaz1:      .ascii "Unesite bazu broja:\0"
ulaz1_duz = . - ulaz1
ulaz2:      .ascii "Unesite broj:\0"
ulaz2_duz = . - ulaz2
ulaz3:      .ascii "Unesite bazu rezultata:\0"
ulaz3_duz = . - ulaz3
izlaz1:     .ascii "Rezultat:\0"
izlaz1_duz = . - izlaz1
greska1:    .ascii "Greska: pogresan znak!\0"
greska1_duz = . - greska1
greska2:    .ascii "Greska: prekoracenje!\0"
greska2_duz = . - greska2

greska: .long 0
buffer_max_duz = 50
buffer: .fill buffer_max_duz, 1, 42
buffer_duz: .long 0

baza: .long 0
broj1: .long 0
broj2: .long 0
rezultat: .long 0

.macro UNOS adresa, duzina, adresa_duz
    movl $3, %eax
    movl $0, %ebx
    movl \adresa, %ecx
    movl \duzina, %edx
    int $0x80
    movl %eax, \adresa_duz
    decl %eax
    movb $0, buffer(, %eax, 1)
.endm
.macro ISPIS adresa, duzina
    movl $4, %eax
    movl $1, %ebx
    movl \adresa, %ecx
    movl \duzina, %edx
    int $0x80
.endm

.section .text
.globl main
main:
    ISPIS $ulaz1, $ulaz1_duz
    UNOS $buffer, $buffer_max_duz, buffer_duz
    # int str_to_int(char* str, unsigned int* greska, unsigned int baza)
    pushl $10
    pushl $greska
    pushl $buffer
    call str_to_int
    movl %eax, baza
    addl $12, %esp
    cmpl $1, greska
    je pogresan_unos
    ja prekoracenje

    ISPIS $ulaz2, $ulaz2_duz
    UNOS $buffer, $buffer_max_duz, buffer_duz
    # int str_to_int(char* str, unsigned int* greska, unsigned int baza)
    pushl baza
    pushl $greska
    pushl $buffer
    call str_to_int
    movl %eax, broj1
    addl $12, %esp
    cmpl $1, greska
    je pogresan_unos
    ja prekoracenje

    ISPIS $ulaz1, $ulaz1_duz
    UNOS $buffer, $buffer_max_duz, buffer_duz
    # int str_to_int(char* str, unsigned int* greska, unsigned int baza)
    pushl $10
    pushl $greska
    pushl $buffer
    call str_to_int
    movl %eax, baza
    addl $12, %esp
    cmpl $1, greska
    je pogresan_unos
    ja prekoracenje
    ISPIS $ulaz2, $ulaz2_duz
    UNOS $buffer, $buffer_max_duz, buffer_duz
    # int str_to_int(char* str, unsigned int* greska, unsigned int baza)
    pushl baza
    pushl $greska
    pushl $buffer
    call str_to_int
    movl %eax, broj2
    addl $12, %esp
    cmpl $1, greska
    je pogresan_unos
    ja prekoracenje

    movl broj1, %eax
    addl broj2, %eax
    jc prekoracenje
    movl %eax, rezultat

    # movl broj2, %eax
    # movl %eax, rezultat
    jmp kraj

pogresan_unos:
    ISPIS $greska1, $greska1_duz
    jmp kraj
prekoracenje:
    ISPIS $greska2, $greska2_duz
    jmp kraj
kraj:
    movl $1, %eax
    movl rezultat, %ebx
    int $0x80

