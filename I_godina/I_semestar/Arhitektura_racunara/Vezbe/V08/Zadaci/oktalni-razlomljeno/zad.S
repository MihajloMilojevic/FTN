# autor: Mihajlo Milojevic SV57/2023
# datum: 14.12.2023.
#                                   +8              +12
# unsigned int oct_str_float_to_inter(char* str, unsigned int* greska);

.section .text
.globl oct_str_float_to_inter
oct_str_float_to_inter: 
    pushl %ebp
    movl %esp, %ebp
    pushl $100000000
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 12(%ebp), %eax
    movl $0, (%eax)
    movl $8, %ecx
    movl $0, %ebx
    movl $0, %eax
    movl $0, %edx
    movl 8(%ebp), %esi
    addl $2, %esi
    movl %esi, %edi
    cmpb $0, (%esi)
    je greska

do_kraja:
    cmpb $0, (%esi)
    je kovnverzija
    incl %esi
    jmp do_kraja

kovnverzija:
    decl %esi

petlja:
    cmpl %edi, %esi
    jb kraj
    movb (%esi), %bl
    subb $'0', %bl
    js greska
    cmpl %ecx, %ebx
    jae greska
    xchgl %eax, %ebx
    mull -4(%ebp)
    jc prekoracenje
    addl %ebx, %eax
    jc prekoracenje
    movl $0, %ebx
    movl $0, %edx
    divl %ecx
    decl %esi
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
    popl %edi
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret