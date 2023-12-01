# autor: Mihajlo Milojevic SV57-2023
#                       +8                +12
# int InvertBits(unsigned int* indeksi, int n);

.section .text
.globl InvertBits
InvertBits:
    pushl %ebp
    movl %esp, %ebp
    pushl %esi
    pushl %ebx
    # povratna vrednost
    movl $0, %eax
    # adrsa prvog elementa niza
    movl 8(%ebp), %ebx
    # brojac
    movl $0, %esi
petlja:
    cmpl %esi, 12(%ebp)
    je return
    movb (%ebx), %cl # vresnost trenutnog elementa niza
    movl $1, %edx   # maska
    shll %cl, %edx
    orl %edx, %eax # postavljamo odgovarajuci bit na 1
post:
    incl %esi
    addl $4, %ebx
    jmp petlja

return:
    popl %ebx
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret
