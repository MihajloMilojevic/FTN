#Opis: Sortira niz
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 26.10.2023.

.section .data
N = 10
niz: .word 5, 6, 7, 10, 9, 1, 3, 2, 4, 8
.section .text
.globl main
main:
    movl $0, %esi
    movl $0, %edi

spoljasnja:                     # spoljasnja petlja for(i = 0; i < n-1; i++)
    cmpl $N-1, %esi
    jnb kraj
    movl %esi, %edi
    inc %edi
unutrasnja:                     # unutrasnja petlja for(j = i+1; j < n; j++)
    cmpl $N, %edi 
    jnb post_s
    movw niz(, %esi, 2), %ax   # ax = niz[i]
    cmpw %ax, niz(, %edi, 2)   # if(niz[j]<niz[i])
    jnb post_u
    movw niz(, %edi, 2), %bx   # bx = niz[j]
    movw %bx, niz(, %esi, 2)   # niz[i] = bx = niz[j]
    movw %ax, niz(, %edi, 2)   # niz[j] = ax = niz[i]
post_u:
    incl %edi
    jmp unutrasnja
post_s:
    incl %esi
    jmp spoljasnja

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


