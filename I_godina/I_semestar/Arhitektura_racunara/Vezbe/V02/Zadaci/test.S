#Opis: Prikazivanje bajtova long promenljive
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 19.10.2023

.section .data
a: .long 0x12345678

.section .text
.globl main
main:
    movb a, %al
    movb a+1, %bl
    movb a+2, %cl
    movb a+3, %dl
    
    jmp kraj
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


