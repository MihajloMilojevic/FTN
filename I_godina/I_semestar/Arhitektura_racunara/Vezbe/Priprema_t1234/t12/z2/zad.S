#autor: Mihajlo Milojevic SV57/2023

.section .data
ulaz_str: .ascii "Unesite string: \0"
ulaz_str_duz = . - ulaz_str
izlaz_str: .ascii "Rezultujuci string: \0"
izlaz_str_duz = . - izlaz_str

unos_max = 50
string: .fill unos_max, 1, 42
duzina_str: .long 0 

.section .text
.globl main
main:
    movl $4, %eax
    movl $3, %ebx
    movl $ulaz_str, %ecx
    movl $unos_max, %edx
    int 0x80

kraj:
    movl $1, %eax
    movl $0, %ebx
    int 0x80
