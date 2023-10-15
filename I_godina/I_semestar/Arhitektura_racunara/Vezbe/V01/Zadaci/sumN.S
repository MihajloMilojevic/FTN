#Opis: Program koji racuna zbir prvih n prirodnih brojeva
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 15.10.2023.

.section .data
.section .text
.globl main
main:
    movl $5, %eax       #n = 5;
    movl $0, %ebx       #rez = 0;

uslov:                  #while(true) {
    cmpl $0, %eax       #if(n == 0)
    je kraj             # break;
    addl %eax, %ebx     # rez+=n;
    subl $1, %eax       # n--;
    jmp uslov           #}
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


