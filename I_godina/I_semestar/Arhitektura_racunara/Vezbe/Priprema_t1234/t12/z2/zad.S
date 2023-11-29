#autor: Mihajlo Milojevic SV57/2023

.section .data
ulaz_str: .ascii "Unesite string: \0"
ulaz_str_duz = . - ulaz_str
izlaz_str: .ascii "Rezultujuci string: \0"
izlaz_str_duz = . - izlaz_str

unos_max = 50
string: .fill unos_max, 1, 42
duzina_str: .long 0 

tacka: .long 0

.section .text
.globl main
main:
    movl $4, %eax
    movl $2, %ebx
    movl $ulaz_str, %ecx
    movl $ulaz_str_duz, %edx
    int $0x80

    movl $3, %eax
    movl $1, %ebx
    movl $string, %ecx
    movl $unos_max, %edx
    int $0x80

    movl %eax, duzina_str

    movl $0, %esi
petlja:
    cmpl %esi, duzina_str
    je kraj
    movb string(, %esi, 1), %al 
    cmpb $'.', %al
    je char_tacka
    cmpl $0, tacka
    je post
    cmpb $'a', %al
    jb post
    cmpb $'z', %al
    ja post

malo_slovo:
    subb $'a', %al
    add $'A', %al
    movb %al, string(, %esi, 1)
    movl $0, tacka
    jmp post


char_tacka:
    movl $1, tacka
    jmp post

post:
    incl %esi
    jmp petlja

kraj:

    movl $4, %eax
    movl $2, %ebx
    movl $izlaz_str, %ecx
    movl $izlaz_str_duz, %edx
    int $0x80

    movl $4, %eax
    movl $2, %ebx
    movl $string, %ecx
    movl duzina_str, %edx
    int $0x80

    movl $1, %eax
    movl $0, %ebx
    int $0x80
