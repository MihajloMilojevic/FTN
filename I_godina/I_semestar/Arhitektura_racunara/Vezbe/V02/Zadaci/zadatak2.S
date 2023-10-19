#Opis: Monozenje dve promenljive i cuvanje rezultata u trecu
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 19.10.2023

.section .data
a: .long 3
b: .long 5
c: .long 0
.section .text
.globl main
main:
    movl a, %eax
    cmpl %eax, b
    ja mnozi # a < b
    movl b, %ebx
    movl %ebx, a 
    movl %eax, b
    jmp mnozi

mnozi:
    movl a, %eax
    movl b, %ebx
    uslov: 
        cmpl $0, %eax
        je kraj         # a = 0
        addl %ebx, c
        decl %eax
        jmp uslov

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


