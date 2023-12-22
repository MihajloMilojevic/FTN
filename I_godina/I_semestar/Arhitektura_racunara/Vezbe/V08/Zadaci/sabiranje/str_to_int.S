# autor: Mihajlo Milojevic SV57/2023
# datum: 14.12.2023.
#                          +8              +12          +16
# int str_to_int(char* str, unsigned int* greska, unsigned int baza)

.section .text
.globl str_to_int
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
    mull %ecx
    jc str_to_int_prekoracenje
    addl %ebx, %eax
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
    jmp kraj

str_to_int_kraj:
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

# int str_to_int_vrednost_znaka(uzima vrednost iz %ebx); return vrednost ili -1
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
    ret
