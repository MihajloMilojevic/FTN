# autor: Mihajlo Milojevic SV57/2023
# datum: 14.12.2023.
#                          +8              +12          +16
# int str_to_inter(char* str, unsigned int* greska, unsigned int baza)

.section .text
.globl str_to_inter
str_to_inter: 
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
    cmpb $'-', (%esi)
    je predznak
    cmpb $'+', (%esi)
    je predznak
    jmp petlja

predznak:
    incl %esi
    cmpb $0, (%esi)
    je greska

petlja:
    movb (%esi), %bl
    cmpb $0, %bl
    je znak
    subb $'0', %bl
    js greska
    cmpl %ecx, %ebx
    jae greska
    mull %ecx
    jc prekoracenje
    addl %ebx, %eax
    jc prekoracenje
    incl %esi
    cmpl $0x80000000, %eax
    je petlja
    testl $0x80000000, %eax
    jnz prekoracenje
    jmp petlja

znak:
    movl 8(%ebp), %esi
    cmpb $'-', (%esi)
    je minus
plus:
    testl $0x80000000, %eax
    jnz prekoracenje
    jmp kraj

minus:
    negl %eax
    jmp kraj


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

# int vrednost_znaka(char *karakter, unsigned int baza, int *greska); return vrednost i greska na 0 ili 1
vrednost_znaka:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx
    pushl %ecx
    pushl %edx

    movl 8(%ebp), %eax
    movl $0, %ecx       
    movb (%eax), %cl            # char
    movl 12(%ebp), %ebx         # base
    movl 16(%ebp), %edx         # error adress
    movl $0, %edx
    cmpl $10, %ebx
    ja vrednost_znaka_veca_baza

    subl $'0', %ebx
    js vrednost_znaka_greska
    cmpl %ebx, %ecx
    jae vrednost_znaka_greska
    movl %ebx, %eax
    jmp vrednost_znaka_kraj

vrednost_znaka_veca_baza:
    cmpb $'0', %bl
    jb vrednost_znaka_ne_cifra
    cmpb $'9', %bl
    ja vrednost_znaka_ne_cifra
    subl $'0', %eax
    movl %ebx, %eax
    jmp vrednost_znaka_kraj
vrednost_znaka_ne_cifra:
    cmpb $'a', %bl
    jb vrednost_znaka_ne_malo
    cmpb $'z', %bl
    ja vrednost_znaka_ne_malo
    

vrednost_znaka_greska:
    movl $1, (%edx)
    jmp vrednost_znaka_kraj

vrednost_znaka_kraj:
    popl %edx
    popl %ecx
    popl %ebx
    popl %ebp
    ret

# int vrednost_char(char *karakter, unsigned int baza); return vrednost karaktera