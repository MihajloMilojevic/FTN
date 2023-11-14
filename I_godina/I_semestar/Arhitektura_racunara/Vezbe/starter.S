# Opis: 
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 

.section .data
.section .text
.globl main
main:
    
    jmp kraj
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


