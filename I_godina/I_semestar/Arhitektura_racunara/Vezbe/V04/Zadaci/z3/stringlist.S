

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
    
    movl $strings, %esi
    movl $0, %edi

petlja_unos:
    cmpl $str_num, %edi
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
    movl %esi, %ecx
    movl $str_len, %edx
    int $0x80

    movl %eax, str_lens(, %edi, 4)

    addl $str_len, %esi
    incl %edi
    jmp petlja_unos

ispis:

    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal str_ispis, %ecx
    movl $n_ip, %edx
    int $0x80
    
    movl $strings, %esi
    addl $str_len*9, %esi
    movl $9, %edi

petlja_ispis:
    cmpl $0, %edi
    jl kraj

    

    # ispis str
    movl $4, %eax
    movl $0, %ebx
    movl %esi, %ecx
    movl str_lens(, %edi, 4), %edx
    int $0x80

    subl $str_len, %esi
    decl %edi
    jmp petlja_ispis

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


