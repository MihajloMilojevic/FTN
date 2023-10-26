#Opis: Aritmeticka sredina niza
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 26.10.2023.

.section .data
N = 10
niz: .long 1,2,3,4,5,6,7,8,9,10
sredina_celo: .long 0
sredina_ost: .long 0
.section .text
.globl main
main:

    movl $0, %esi           # trenutni index 
    movl $0, %eax           # cuva se suma
petlja:                     # sabira elemente u opsegu [ind1, ind2)
    addl niz(, %esi, 4), %eax
    incl %esi
    cmpl $N, %esi           # proverava trenutni index sa N 
    jb petlja               # izvrsava petlju dokle god je index < N

deli:
    movl $0, %edx
    movl $N, %ecx
    divl %ecx
    movl %eax, sredina_celo
    movl %edx, sredina_ost

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


