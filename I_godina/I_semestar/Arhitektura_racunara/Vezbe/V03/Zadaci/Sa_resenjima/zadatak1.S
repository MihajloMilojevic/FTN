#Opis: Suma elemenata podniza
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 26.10.2023.

.section .data
N = 10
niz: .long 1,2,3,4,5,6,7,8,9,10
suma: .long 0
ind1: .long 0
ind2: .long 0
.section .text
.globl main
main:
    movl $2, ind1           # pocetna vrednost indexa 1
    movl $6, ind2           # pocetna vrednost indexa 2

    movl ind1, %esi         # trenutni index, pocevsi od ind1
    movl $0, %eax           # cuva se suma
petlja:                     # sabira elemente u opsegu [ind1, ind2)
    addl niz(, %esi, 4), %eax
    incl %esi
    cmpl ind2, %esi         # proverava trenutni index sa ind2 
    jb petlja               # izvrsava petlju dokle god je index < ind2
kraj:
    movl %eax, suma
    movl $1, %eax
    movl $0, %ebx
    int $0x80


