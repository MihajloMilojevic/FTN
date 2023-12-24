# autor: Mihajlo Milojevic SV57/2023
# fajlovi: zad.S

# Ako vaše rešenje sadrži dodatne fajlove, stavite njihove nazive u liniju fajlovi
# Na primer, ako imate i potprogram u pp.S, iza fajlovi treba da stoji: zad.S pp.S

.section .data
poruka_unos: .ascii "Unesite jednacinu: "
poruka_unos_duz = . - poruka_unos
poruka_resenje: .ascii "Resenje: x = "
poruka_resenje_duz = . - poruka_resenje
poruka_greska_konverzija: .ascii "Greska pri konverziji!\n"  # Kod greske = 1
poruka_greska_konverzija_duz = . - poruka_greska_konverzija
poruka_greska_operand: .ascii "Greska! Neispravna operacija!\n"  # Kod greske = 2
poruka_greska_operand_duz = . - poruka_greska_operand

kod_greske: .long 0

max_duz = 50
buffer: .fill max_duz, 1, 42
buffer_duz: .long 0

operacija: .ascii "!"
prvi: .long 0
drugi: .long 0
rezultat: .long 0


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
    ISPIS $poruka_unos, $poruka_unos_duz
    UNOS $buffer, $max_duz, buffer_duz

    movl $buffer, %esi
razmak:
    cmpb $0, (%esi)
    je obrada
    cmpb $' ', (%esi)
    je obrada
    incl %esi
    jmp razmak

obrada:
    movb $0, (%esi)
    incl %esi
    pushl $prvi
    pushl $buffer
    call str_to_int
    addl $8, %esp
    movl %eax, kod_greske
    cmpl $0, %eax
    ja greska_operand

    movb (%esi), %al
    movb %al, operacija

    addl $6, %esi
    pushl $drugi
    pushl %esi
    call str_to_int
    addl $8, %esi
    movl %eax, kod_greske
    cmpl $0, %eax
    ja greska_operand

    cmpb $'-', operacija
    je minus
    cmpb $'+', operacija
    je plus
    jmp greska_operacija

plus:
    movl drugi, %eax
    subl prvi, %eax
    movl %eax, rezultat
    jmp print
minus:
    movl prvi, %eax
    subl drugi, %eax
    movl %eax, rezultat
    jmp print
print:
    pushl rezultat
    pushl $buffer
    call int_to_str
    addl $8, %esp
    movl %eax, buffer_duz
    ISPIS $poruka_resenje, $poruka_resenje_duz
    ISPIS $buffer, buffer_duz
    movl $0, kod_greske
    jmp kraj

greska_operand:
    movl $1, kod_greske
    ISPIS $poruka_greska_konverzija, $poruka_greska_konverzija_duz
    jmp kraj
    
greska_operacija:
    movl $2, kod_greske
    ISPIS $poruka_greska_operand, $poruka_greska_operand_duz
    jmp kraj

kraj:
    movl $1, %eax
    movl kod_greske, %ebx
    int $0x80

#                   +8              +12
# int str_to_int(char* string, int* broj) -> vraca gresku
str_to_int:
    pushl %ebp
    movl %esp, %ebp
    pushl $0
    pushl %esi
    pushl %ebx
    pushl %ecx
    pushl %edx
    movl $10, %ebx          # baza
    movl 8(%ebp), %esi      # adresa trenutnog karaktera
    movl $0, %eax           # rezultat

str_to_int_loop:
    xorl %ecx, %ecx
    movb (%esi), %cl
    cmpb $0, %cl
    je str_to_int_end
    subb $'0', %cl
    js str_to_int_err
    cmpb $9, %cl
    ja str_to_int_err
    mull %ebx
    addl %ecx, %eax
    incl %esi
    jmp str_to_int_loop

str_to_int_err:
    incl -4(%ebp)

str_to_int_end:
    movl 12(%ebp), %ecx
    movl %eax, (%ecx)
    movl -4(%ebp), %eax
    popl %edx
    popl %ecx
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret
#                       +8          +12
# int int_to_str(char *string, int broj) -> duzina
int_to_str:
    pushl %ebp
    movl %esp, %ebp
    pushl %esi
    pushl %edi
    pushl %ebx
    pushl %ecx
    pushl %edx

    movl 12(%ebp), %eax         # broj
    movl $10, %ebx              # baza
    movl 8(%ebp), %esi          # pocetak stringa
    movl 8(%ebp), %edi          # pocetak stringa

    cmpl $0, %eax 
    je int_to_str_nula
    jl int_to_str_neg
    jmp int_to_str_conv

int_to_str_nula:
    movb $'0', (%esi)
    movb $0, 1(%esi)
    movl $1, %eax
    jmp int_to_str_end
int_to_str_neg:
    movb $'-', (%esi)
    incl %esi
    incl %edi
    negl %eax
    jmp int_to_str_conv

int_to_str_conv:
    xorl %edx, %edx
    divl %ebx
    addb $'0', %dl
    movb %dl, (%esi)
    incl %esi
    cmpl $0, %eax
    ja int_to_str_conv

    movl $0, (%esi)
    movl %esi, %eax
    subl 8(%ebp), %eax      # duzina stringa
    decl %esi
int_to_str_rev:
    cmpl %edi, %esi
    jbe int_to_str_end
    movb (%esi), %bl
    movb (%edi), %bh
    movb %bh, (%esi)
    movb %bl, (%edi)
    incl %edi
    decl %esi
    jmp int_to_str_rev

int_to_str_end:
    popl %edx
    popl %ecx
    popl %ebx
    popl %edi
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret