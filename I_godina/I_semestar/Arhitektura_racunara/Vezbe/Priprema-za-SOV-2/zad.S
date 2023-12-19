# autor: Mihajlo Milojevic SV57/2023
.section .data
prompt1: .ascii "Unseite logicki izraz: \0"
prompt1_duz = . - prompt1
prompt2: .ascii "Rezultat: \0"
prompt2_duz = . - prompt2
err1: .ascii "Greska kod operanda.\n\0"
err1_duz = . - err1
err2: .ascii "Greska kod operacije.\n\0"
err2_duz = . - err2
newline: .ascii "\n\0"
newline_duz = . - newline

max_duz = 100
unos: .fill max_duz, 1, 42
.byte 0
unos_duz: .long 0

buffer: .fill max_duz, 1, 42
.byte 0
buffer_duz: .long 0

greska: .long 0



.macro ISPIS adresa, duzina
    movl $4, %eax
    movl $1, %ebx
    movl \adresa, %ecx
    movl \duzina, %edx
    int $0x80
.endm
.macro UNOS adresa, duzina, uneseno
    movl $3, %eax
    movl $0, %ebx
    movl \adresa, %ecx
    movl \duzina, %edx
    int $0x80
    decl %eax
    movl %eax, \uneseno
    movl \adresa, %ebx
    movb $0, (%ebx ,%eax,1)
.endm

.section .text
.globl main

main:
    ISPIS $prompt1, $prompt1_duz
    UNOS $unos, $max_duz, unos_duz

    ISPIS $unos, unos_duz
    ISPIS $newline, $newline_duz

kraj:
    movl $1, %eax
    movl greska, %ebx
    int $0x80

%
str_to_int:
