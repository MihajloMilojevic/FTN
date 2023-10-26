#Opis: 
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 

.section .data
const = 20
.section .text
.globl main
main:
    movl $1, const
    jmp kraj
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


