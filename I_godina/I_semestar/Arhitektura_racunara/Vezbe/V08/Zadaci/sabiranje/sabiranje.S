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
newline:    .ascii "\n\0"
newline_duz = . - newline

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
    # broj 1
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

    # broj 2
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

    movl broj1, %eax
    addl broj2, %eax
    jc prekoracenje
    movl %eax, rezultat

    # unsigned int int_to_str(unsigned int broj, char* str, unsigned int duzina, unsigned int baza, unsigned int* greska);
    pushl $greska
    pushl baza
    pushl $buffer_max_duz
    pushl $buffer
    pushl rezultat
    call int_to_str
    movl %eax, buffer_duz
    addl $16, %esp
    cmpl $0, greska
    ja prekoracenje
    ISPIS $izlaz1, $izlaz1_duz
    ISPIS $buffer, buffer_duz
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
    ISPIS $newline, $newline_duz
    movl $1, %eax
    movl $0, %ebx
    int $0x80



str_to_int: 
    pushl %ebp
    movl %esp, %ebp
    pushl %esi
    pushl %ebx

    movl 12(%ebp), %eax
    movl $0, (%eax)
    movl 16(%ebp), %ecx
    movl $0, %ebx
    movl $0, %eax
    movl 8(%ebp), %esi
    cmpb $0, (%esi)
    je str_to_int_greska

str_to_int_petlja:
    movb (%esi), %bl
    cmpb $0, %bl
    je str_to_int_kraj
    call vrednost_znaka
    js str_to_int_greska
    cmpl %ecx, %ebx
    jae str_to_int_greska
    mull %ecx
    jc str_to_int_prekoracenje
    addl %ebx, %eax
    jc str_to_int_prekoracenje
    incl %esi
    jmp str_to_int_petlja

str_to_int_greska:
    movl 12(%ebp), %eax
    movl $1, (%eax)
    jmp str_to_int_kraj
str_to_int_prekoracenje:
    movl 12(%ebp), %eax
    movl $2, (%eax)
    jmp str_to_int_kraj

str_to_int_kraj:
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

# int vrednost_znaka(uzima vrednost iz %ebx); return vrednost ili -1
vrednost_znaka:
    cmpl $0, %ebx
    je vrednost_znaka_kraj
    cmpl $'0', %ebx
    jb vrednost_znaka_malo
    cmpl $'9', %ebx
    ja vrednost_znaka_malo
    subl $'0', %ebx
    jmp vrednost_znaka_kraj
vrednost_znaka_malo:
    orl $0b100000, %ebx
    cmpl $'a', %ebx
    jb vrednost_znaka_greska
    cmpl $'z', %ebx
    ja vrednost_znaka_greska
    subl $'a', %ebx
    addl $10, %ebx
    jmp vrednost_znaka_kraj
vrednost_znaka_greska:
    movl $-1, %ebx
vrednost_znaka_kraj:
    ret

int_to_str:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # int_to_str_greska
    pushl $0     # duzina
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl 20(%ebp), %ebx           # baza
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera

int_to_str_konvertuj:
    cmpl $1, %edi
    jbe int_to_str_greska
    xorl %edx, %edx
    divl %ebx
    cmpb $9, %dl
    ja int_to_str_slovo
int_to_str_cifra:
    addb $'0', %dl
    jmp int_to_str_nastavak
int_to_str_slovo:
    subb $10, %dl
    addb $'a', %dl

int_to_str_nastavak:
    movb %dl, (%esi)
    incl %esi
    incl -8(%ebp)
    decl %edi
    cmpl $0, %eax
    jne int_to_str_konvertuj
    movb $0, (%esi)             # \0 na int_to_str_kraj stringa
    decl %esi                   # vrati pokazivac na poslednji karakter u stringu
    movl 12(%ebp), %edi         # adresa prvog karaktera
int_to_str_obrni:
    cmpl %edi, %esi
    jbe int_to_str_kraj
    movb (%esi), %al
    movb (%edi), %ah
    movb %ah, (%esi)
    movb %al, (%edi)
    incl %edi
    decl %esi
    jmp int_to_str_obrni


int_to_str_greska:
    incl -4(%ebp)
    jmp int_to_str_kraj

int_to_str_kraj:

    movl 24(%ebp), %eax
    movl -4(%ebp), %ebx
    movl %ebx, (%eax)
    movl -8(%ebp), %eax
    popl %ebx
    popl %edi
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret