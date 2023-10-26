#Opis: Izbacivanje razmaka sa pocetka i kraja stringa
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 26.10.2023.

.section .data
str: .ascii "   abcd    \0"
.section .text
.globl main
main:
    movl $str, %eax
# sa slajdova - izbacivanje sa kraja
kraj_s: 
    cmpb $0, (%eax)
    je razmaci_k
    incl %eax
    jmp kraj_s
razmaci_k:
    cmpb $' ', -1(%eax)
    jne izbaci_k
    decl %eax
    jmp razmaci_k
izbaci_k:
    movb $0, (%eax)

# izbacivanje sa pocetka
pocetak: 
    movl $str, %eax             # eax pokazuje na pocetak
pronadji_prvi:                  # trazimo prvi ne razmak
    cmpb $' ', (%eax)
    jne pomeraj
    incl %eax
    jmp pronadji_prvi
pomeraj:
    movl $str, %ebx             # ebx pokazuje na pocetak stringa
uslov:
    cmpb $0, %eax               # dok ne dodjemo do kraja stringa pomeraj iz eax u ebx
    je kraj
    movl (%eax), %ecx
    movb %ecx, (%ebx)
    incl %eax
    incl %ebx
    jmp uslov

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

