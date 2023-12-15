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
    je greska

petlja:
    movb (%esi), %bl
    cmpb $0, %bl
    je kraj
    call vrednost_znaka
    js greska
    cmpl %ecx, %ebx
    jae greska
    mull %ecx
    jc prekoracenje
    addl %ebx, %eax
    jc prekoracenje
    incl %esi
    jmp petlja

greska:
    movl 12(%ebp), %eax
    movl $1, (%eax)
    jmp kraj
prekoracenje:
    movl 12(%ebp), %eax
    movl $2, (%eax)
    jmp kraj

kraj:
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret

# int vrednost_znaka(uzima vrednost iz %ebx); return vrednost ili -1
vrednost_znaka:
    cmpl $0, %ebx
    je vrednost_znaka_kraj
    cmpl $'0', %ebx
    jb vrednost_znaka_malo
    cmpl $'9', %ebx
    ja vrednost_znaka_malo
    subl $'0', %ebx
    jmp vrednost_znaka_kraj
vrednost_znaka_malo:
    orl $0b100000, %ebx
    cmpl $'a', %ebx
    jb vrednost_znaka_greska
    cmpl $'z', %ebx
    ja vrednost_znaka_greska
    subl $'a', %ebx
    addl $10, %ebx
    jmp vrednost_znaka_kraj
vrednost_znaka_greska:
    movl $-1, %ebx
vrednost_znaka_kraj:
    ret
