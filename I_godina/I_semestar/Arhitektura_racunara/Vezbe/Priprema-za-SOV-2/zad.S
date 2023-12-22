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

ind: .long 0

rezultat: .byte 0
operand: .byte 0



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
    incl %edx
    int $0x80
    decl %eax
    movl %eax, \uneseno
    movl \adresa, %ebx
    movb $0, (%ebx ,%eax,1)
.endm
.macro OPERACIJA naredba
    pushl $buffer
    pushl ind
    call extract
    addl $8, %esp
    addl %eax, ind
    incl ind
    pushl %eax
    pushl $greska
    pushl $buffer
    call convert
    addl $12, %esp
    movb %al, operand
    cmpl $0, greska
    ja operand_err
    movb operand, %cl
    \naredba %cl, rezultat
    jmp petlja
.endm

.section .text
.globl main

main:
    ISPIS $prompt1, $prompt1_duz
    UNOS $unos, $max_duz, unos_duz

    movl $unos, ind
    pushl $buffer
    pushl ind
    call extract
    addl $8, %esp
    addl %eax, ind
    incl ind
    movl %eax, buffer_duz
    pushl %eax
    pushl $greska
    pushl $buffer
    call convert
    addl $12, %esp
    movb %al, rezultat
    cmpl $0, greska
    ja operand_err

petlja:
    movl ind, %eax
    subl $unos, %eax
    cmpl unos_duz, %eax
    jae print
    pushl $buffer
    pushl ind
    call extract
    addl $8, %esp
    addl %eax, ind
    incl ind      # extract operator
    cmpl $0, %eax
    je print
    cmpb $'<', buffer
    je op_rot_levo
    cmpb $'>', buffer
    je op_rot_desno
    cmpb $'^', buffer
    je op_xor
    jmp operacija_err
op_rot_levo:
    OPERACIJA rolb
op_rot_desno:
    OPERACIJA rorb
op_xor:
   OPERACIJA xorb
    
print:
    movl $0, %eax
    movb rezultat, %al
    pushl $greska
    pushl $8
    pushl $max_duz
    pushl $buffer
    pushl %eax
    call int_to_str
    addl $20, %esp
    ISPIS $prompt2, $prompt2_duz
    ISPIS $buffer, %eax
    ISPIS $newline, $newline_duz
    movl $0, greska
    jmp kraj

operand_err:
    ISPIS $err1, $err1_duz
    movl $1, greska
    jmp kraj
operacija_err:
    ISPIS $err2, $err2_duz
    movl $1, greska
    jmp kraj

kraj:
    movl $1, %eax
    movl greska, %ebx
    int $0x80

# int extract(char *source, char *destinatiion) -> duzinu
extract:
    pushl %ebp
    movl %esp, %ebp
    pushl %esi
    pushl %edi
    pushl %ebx

    movl $0, %ebx
    movl $0, %eax
    movl 8(%ebp), %esi
    movl 12(%ebp), %edi
    cmpb $' ', (%esi)   # trim
    jne extract_loop
    incl %esi

extract_loop:
    movb (%esi), %bl
    cmpb $0, %bl
    je extract_kraj
    cmpb $' ', %bl
    je extract_kraj
    movb %bl, (%edi)
    incl %eax
    incl %esi
    incl %edi
    jmp extract_loop

extract_kraj:
    movl $0, (%edi)
    popl %ebx
    popl %edi
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

# int convert(char *str, unsigned int *greska, int duzina)
convert:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx
    pushl %esi
    movl 8(%ebp), %esi
    cmpl $2, 16(%ebp)
    jbe convert_10
    cmpb $'0', (%esi)
    jne convert_10
    incl %esi
    cmpb $'x', (%esi)
    je convert_16
    cmpb $'X', (%esi)
    je convert_16

convert_10:
    pushl $10
    jmp convert_call
convert_16:
    incl %esi
    pushl $16
convert_call:
    pushl 12(%ebp)
    pushl %esi
    call str_to_int
    addl $12, %esp

convert_kraj:
    popl %esi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret

#                          +8              +12          +16
# int str_to_int(char* str, unsigned int* greska, unsigned int baza)
str_to_int: 
    pushl %ebp
    movl %esp, %ebp
    pushl %esi
    pushl %ebx

    movl 12(%ebp), %eax
    movl $0, (%eax)
    movl 16(%ebp), %ecx
    movl $0, %ebx
    movl $0, %eax
    movl 8(%ebp), %esi
    cmpb $0, (%esi)
    je str_to_int_greska

str_to_int_petlja:
    movb (%esi), %bl
    cmpb $0, %bl
    je str_to_int_kraj
str_to_int_vrednost_znaka:
    cmpl $0, %ebx
    je str_to_int_vrednost_znaka_kraj
    cmpl $'0', %ebx
    jb str_to_int_vrednost_znaka_malo
    cmpl $'9', %ebx
    ja str_to_int_vrednost_znaka_malo
    subl $'0', %ebx
    jmp str_to_int_vrednost_znaka_kraj
str_to_int_vrednost_znaka_malo:
    orl $0b100000, %ebx
    cmpl $'a', %ebx
    jb str_to_int_vrednost_znaka_str_to_int_greska
    cmpl $'z', %ebx
    ja str_to_int_vrednost_znaka_str_to_int_greska
    subl $'a', %ebx
    addl $10, %ebx
    jmp str_to_int_vrednost_znaka_kraj
str_to_int_vrednost_znaka_str_to_int_greska:
    movl $-1, %ebx
str_to_int_vrednost_znaka_kraj:
    cmpl $0, %ebx
    jl str_to_int_greska
    cmpl %ecx, %ebx
    jae str_to_int_greska
    mulb %cl
    jc str_to_int_prekoracenje
    addb %bl, %al
    jc str_to_int_prekoracenje
    incl %esi
    jmp str_to_int_petlja

str_to_int_greska:
    movl 12(%ebp), %eax
    movl $1, (%eax)
    jmp str_to_int_kraj
str_to_int_prekoracenje:
    movl 12(%ebp), %eax
    movl $2, (%eax)
    jmp str_to_int_kraj

str_to_int_kraj:
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

# unsigned int int_to_str(unsigned int broj, char* str, unsigned int duzina, unsigned int baza, unsigned int *int_to_str_greska);
int_to_str:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # int_to_str_greska
    pushl $0     # duzina
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl 20(%ebp), %ebx           # baza
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera

int_to_str_konvertuj:
    cmpl $1, %edi
    jbe int_to_str_greska
    xorl %edx, %edx
    divl %ebx
    cmpb $9, %dl
    ja int_to_str_slovo
int_to_str_cifra:
    addb $'0', %dl
    jmp int_to_str_nastavak
int_to_str_slovo:
    subb $10, %dl
    addb $'a', %dl

int_to_str_nastavak:
    movb %dl, (%esi)
    incl %esi
    incl -8(%ebp)
    decl %edi
    cmpl $0, %eax
    jne int_to_str_konvertuj
    movb $0, (%esi)             # \0 na int_to_str_kraj stringa
    decl %esi                   # vrati pokazivac na poslednji karakter u stringu
    movl 12(%ebp), %edi         # adresa prvog karaktera
int_to_str_obrni:
    cmpl %edi, %esi
    jbe int_to_str_kraj
    movb (%esi), %al
    movb (%edi), %ah
    movb %ah, (%esi)
    movb %al, (%edi)
    incl %edi
    decl %esi
    jmp int_to_str_obrni


int_to_str_greska:
    incl -4(%ebp)
    jmp int_to_str_kraj

int_to_str_kraj:

    movl 24(%ebp), %eax
    movl -4(%ebp), %ebx
    movl %ebx, (%eax)
    movl -8(%ebp), %eax
    popl %ebx
    popl %edi
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret