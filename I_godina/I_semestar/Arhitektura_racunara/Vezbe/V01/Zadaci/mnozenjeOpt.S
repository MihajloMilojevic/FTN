#Opis: Program mnozi dva prirodna broja koriscenjem visestrukog sabiranja
#      vodeci racuna da se petlja uvek izvrsava manji broj puta
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 15.10.2023.

.section .data
.section .text
.globl main
main:
    movl $5, %eax   # prvi broj - a
    movl $3, %ebx   # drugi broj - b
    movl $0, %ecx   # rezultat - c = a * b

    cmpl %eax, %ebx     # a < b
    ja uslov
    xchgl %eax, %ebx

uslov:
    cmpl $0, %eax
    je kraj
    addl %ebx, %ecx
    subl $1, %eax
    jmp uslov

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


