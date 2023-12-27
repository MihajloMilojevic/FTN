# autor: Imenko Prezimić INDEX ra1234-2016
# fajlovi: zad.S

# Ako vaše rešenje sadrži dodatne fajlove, stavite njihove nazive u liniju fajlovi
# Na primer, ako imate i potprogram u pp.S, iza fajlovi treba da stoji: zad.S pp.S
.section .data
punos: 		.ascii "Unesite string: \0"
punos_duz = . - punos
pgreska: 	.ascii "Doslo je do greske u izvrsavanju programa!\n\0"
pgreska_duz = . - pgreska
psuma: 		.ascii "Suma elemenata niza je: \0"
psuma_duz = . - psuma
pbroj_oktalnih: .ascii "\nBroj oktalnih elemenata u nizu: \0"
pbroj_oktalnih_duz = . - pbroj_oktalnih
pbroj_decimalnih: .ascii "\nBroj decimalnih elemenata u nizu: \0"
pbroj_decimalnih_duz = . - pbroj_decimalnih
pnovi_red: 	.ascii "\n\0"
pnovi_red_duz = . - pnovi_red

kod_greske: .long 0

buffer_max = 30
buffer: .fill buffer_max, 1, 42
buffer_duz: .long 0

suma: .long 0
decimalnih: .long 0
oktalnih: .long 0

.macro ISPIS adresa, duzina
    movl $4, %eax
    movl $1, %ebx
    movl \adresa, %ecx
    movl \duzina, %edx
    int $0x80
.endm
.macro UNOS adresa, duzina, uneseno
    movl $3, %eax
    movl $0, %ebx
    movl \adresa, %ecx
    movl \duzina, %edx
    incl %edx
    int $0x80
    decl %eax
    movl %eax, \uneseno
    movl \adresa, %ebx
    movb $0, (%ebx ,%eax,1)
.endm
.macro REZ broj
    pushl $kod_greske
    pushl $10
    pushl $buffer_max
    pushl $buffer
    pushl \broj
    call int_to_str
    addl $20, %esp
    movl %eax, buffer_duz
    ISPIS $buffer, buffer_duz
.endm
.section .text
.globl main
main:
    ISPIS $punos, $punos_duz
    UNOS $buffer, $buffer_max, buffer_duz
    movl $buffer, %esi
    movl $buffer, %edi
petlja:
    movl %esi, %ebx
    subl $buffer, %ebx
    cmpl buffer_duz, %ebx
    jae print
razmak:
    cmpb $0, (%esi)
    je nastavak
    cmpb $' ', (%esi)
    je nastavak
    incl %esi
    jmp razmak
nastavak:
    movb $0, (%esi)
    movl %esi, %ebx
    subl %edi, %ebx
    pushl %ebx
    pushl %edi
    call odredi_bazu
    addl $8, %esp
    cmpl $8, %eax
    je okt

    incl decimalnih
    jmp konvertuj
okt:
    incl oktalnih

konvertuj:
    pushl %eax
    pushl $kod_greske
    pushl %edi
    call str_to_int
    addl $12, %esp
    cmpl $0, kod_greske
    ja greska
    addl %eax, suma
    jc prekoracenje
    incl %esi
    movl %esi, %edi
    jmp petlja

print:
    ISPIS $psuma, $psuma_duz
    REZ suma
    ISPIS $pbroj_oktalnih, $pbroj_oktalnih_duz
    REZ oktalnih
    ISPIS $pbroj_decimalnih, $pbroj_decimalnih_duz
    REZ decimalnih
    movl $0, kod_greske
    jmp kraj
prekoracenje:
    movl $3, kod_greske
greska:
    ISPIS $pgreska, $pgreska_duz
kraj:
    ISPIS $pnovi_red, $pnovi_red_duz
    movl $1, %eax
    movl kod_greske, %ebx
    int $0x80

#                   +8              +12
# int odredi_bazu(char *string, int duzina) -> bazu broja 8, 10
odredi_bazu:
    pushl %ebp
    movl %esp, %ebp
    pushl %esi

    cmpl $1, 12(%ebp)
    jbe odredi_bazu_10
    movl 8(%ebp), %esi
    cmpb $'0', (%esi)
    je odredi_bazu_8

odredi_bazu_10:
    movl $10, %eax
    jmp odredi_bazu_kraj
odredi_bazu_8:
    movl $8, %eax
    jmp odredi_bazu_kraj

odredi_bazu_kraj:
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

#                          +8              +12          +16
# int str_to_int(char* str, unsigned int* greska, unsigned int baza)
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
    subl $'0', %ebx
    js str_to_int_greska
    cmpl %ecx, %ebx
    jae str_to_int_greska
    mulb %cl
    jc str_to_int_prekoracenje
    addb %bl, %al
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

# unsigned int int_to_str(unsigned int broj, char* str, unsigned int duzina, unsigned int baza, unsigned int *int_to_str_greska);
int_to_str:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # int_to_str_greska
    pushl $0     # duzina
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl 20(%ebp), %ebx     # baza
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera

int_to_str_konvertuj:
    cmpl $1, %edi
    jbe int_to_str_greska
    xorl %edx, %edx
    divl %ebx
    addb $'0', %dl
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