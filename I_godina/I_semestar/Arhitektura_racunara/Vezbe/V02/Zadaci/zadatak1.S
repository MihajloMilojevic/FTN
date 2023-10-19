#Opis: Poredjenje 2 64-bitne vrednosti
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 19.10.2023

.section .data
a: .quad 0x123456789
b: .quad 0x12345678

.section .text
.globl main
main:
    movl $0, %eax
    # poredi vise delove
    movl a, %ebx
    movl b, %ecx
    cmpl %ebx, %ecx
    jg b_vece             # b vece
    jl a_vece             # a vece
    # poredi manje delove
    movl a+4, %ebx
    movl b+4, %ecx
    cmpl %ebx, %ecx
    ja b_vece             # b vece
    jb a_vece             # a vece
    jmp kraj

a_vece: 
    movl $1, %eax
    jmp kraj
b_vece: 
    movl $-1, %eax
    jmp kraj

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


