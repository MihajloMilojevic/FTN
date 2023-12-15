# autor: Mihajlo Milojevic SV57/2023
# datum: 14.12.2023.
#                                   +8              +12
# unsigned int oct_str_to_inter(char* str, unsigned int* greska);

.section .text
.globl oct_str_to_inter
oct_str_to_inter: 
    pushl %ebp
    movl %esp, %ebp
    pushl %esi
    pushl %ebx

    movl 12(%ebp), %eax
    movl $0, (%eax)
    movl $8, %ecx
    movl $0, %ebx
    movl $0, %eax
    movl 8(%ebp), %esi
    cmpb $0, (%esi)
    je greska

petlja:
    movb (%esi), %bl
    cmpb $0, %bl
    je kraj
    subb $'0', %bl
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