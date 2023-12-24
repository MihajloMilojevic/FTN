# autor: Mihajlo Milojevic SV57/2023
# fajlovi: zad.S

# Ako vaše rešenje sadrži dodatne fajlove, stavite njihove nazive u liniju fajlovi
# Na primer, ako imate i potprogram u pp.S, iza fajlovi treba da stoji: zad.S pp.S

.section .data
poruka_unos: .ascii "Unesite zirafin pritisak: "
poruka_unos_duz = . - poruka_unos
poruka_ispis: .ascii "Potrebna korekcija: "
poruka_ispis_duz = . - poruka_ispis
poruka_greska: .ascii "Doslo je do greske pri konverziji!\n"
poruka_greska_duz = . - poruka_greska
newline: .ascii "\n"
newline_duz = . - newline

greska: .long 0
buffer_max = 50
buffer: .fill buffer_max, 1, 42
buffer_duz: .long 0

gornji: .long 0
donji: .long 0


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
    UNOS $buffer, $buffer_max, buffer_duz

    pushl $donji
    pushl $gornji
    pushl $buffer
    call convert
    addl $12, %esp
    cmpl $0, %eax
    ja error

provera_gornjeg:
    cmpl $240, gornji
    jb gornji_nizak
    cmpl $280, gornji
    ja gornji_visok
    movl $0, gornji
    jmp provera_donjeg

gornji_nizak:
    subl $240, gornji
    negl gornji
    jmp provera_donjeg

gornji_visok:
    subl $280, gornji
    negl gornji
    jmp provera_donjeg


provera_donjeg:
    cmpl $160, donji
    jb donji_nizak
    cmpl $200, donji
    ja donji_visok
    movl $0, donji
    jmp rezultat

donji_nizak:
    subl $160, donji
    negl donji
    jmp rezultat

donji_visok:
    subl $200, donji
    negl donji
    jmp rezultat

rezultat:
    pushl donji
    pushl gornji
    pushl $buffer
    call format
    addl $12, %esp
    movl %eax, buffer_duz

    ISPIS $poruka_ispis, $poruka_ispis_duz
    ISPIS $buffer, buffer_duz
    ISPIS $newline, $newline_duz
    jmp end
error:
    movl $1, greska
    ISPIS $poruka_greska, $poruka_greska_duz
end:
    movl $1, %eax
    movl greska, %ebx
    int $0x80

# funkcije

# int convert(char *string, int *broj1, int *broj2) -> vraca gresku 
convert:
    pushl %ebp
    movl %esp, %ebp
    pushl $0        # greska
    pushl %esi
    pushl %ebx
    pushl %ecx
    pushl %edx
    movl 8(%ebp), %esi

convert_loop:
    cmpb $'/', (%esi)
    je convert_loop_end
    incl %esi
    jmp convert_loop

convert_loop_end:
    movb $0, (%esi)         # 123\0456\0
    incl %esi

    pushl 12(%ebp)          # broj1
    pushl 8(%ebp)           # pocetak string
    call str_to_int
    addl $8, %esp
    cmpl $0, %eax
    ja convert_err

    pushl 16(%ebp)          # broj2
    pushl %esi              # pocetak string
    call str_to_int
    addl $8, %esp
    cmpl $0, %eax
    ja convert_err
    jmp convert_end

convert_err:
    incl -4(%ebp)

convert_end:
    movl -4(%ebp), %eax
    popl %edx
    popl %ecx
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

# int format(char *string, int broj1, int broj2) -> duzina
format:
    pushl %ebp
    movl %esp, %ebp
    pushl $1            # duzina
    pushl %esi
    pushl %ebx
    pushl %ecx
    pushl %edx

    movl 8(%ebp), %esi      # string
    movl 12(%ebp), %ecx     # broj1
    movl 16(%ebp), %edx     # broj2
    pushl %ecx
    pushl %esi
    call int_to_str
    addl $8, %esp
    addl %eax, %esi
    addl %eax, -4(%ebp)
    movb $'/', (%esi)
    incl %esi

    pushl %edx
    pushl %esi
    call int_to_str
    addl $8, %esp
    addl %eax, %esi
    addl %eax, -4(%ebp)
    movb $0, (%esi)

format_end:
    movl -4(%ebp), %eax
    popl %edx
    popl %ecx
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

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
    jg int_to_str_poz
    jl int_to_str_neg

int_to_str_nula:
    movb $'0', (%esi)
    movb $0, 1(%esi)
    movl $1, %eax
    jmp int_to_str_end
int_to_str_poz:
    movb $'+', (%esi)
    incl %esi
    incl %edi
    jmp int_to_str_conv
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