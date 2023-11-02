

#Opis: Unos 10 stringova i njihov ispis u obrnutom redu
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 2.11.2023

.section .data
str_unos:   .ascii "Unesite string:\0"
n_up = . - str_unos

str_ispis:  .ascii "\nObrnuti redosled:\n\0"
n_ip = . - str_ispis

str_len = 21    # dužina jednog stringa (20 znakova + Enter)
str_num = 10    # broj stringova
strings: .fill str_len*str_num,1,42

str_lens: .fill str_num,4,0

.section .text
.globl main
main:
    
    movl $0, %esi

petlja_unos:
    cmpl $str_num, %esi
    je ispis

    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal str_unos, %ecx
    movl $n_up, %edx
    int $0x80

    # unesi str
    movl $3, %eax
    movl $0, %ebx
    leal strings(, %esi * $str_len, 1), %ecx
    movl $str_len, %edx
    int $0x80

    movl %eax, str_lens(, %esi, 4)

    incl %esi
    jmp petlja_unos

ispis:
        movl $9, %esi

petlja_ispis:
    cmpl $0, %esi
    je kraj

    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal str_ispis, %ecx
    movl $n_ip, %edx
    int $0x80

    # ispis str
    movl $3, %eax
    movl $0, %ebx
    leal strings(, %esi * $str_len, 1), %ecx
    movl str_lens(, %esi, 4), %edx
    int $0x80

    incl %esi
    jmp petlja_ispis

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


