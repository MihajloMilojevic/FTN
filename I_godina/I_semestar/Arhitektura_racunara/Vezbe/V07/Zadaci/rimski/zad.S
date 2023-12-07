# autor: Mihajlo Milojevic SV57/2023
# datum: 7.12.2023.

# int inter_to_roman(unsigned int broj, char *str, int duzina);

.section .text
.globl inter_to_roman
dec:    .long 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
rom1:   .ascii "MCDCCXLXXIVII"
rom2:   .ascii " M D C L X V "

inter_to_roman:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # greska
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl $0, %ebx           # index
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera

konvertuj:
    cmpl $0, %eax
    je kraj
    cmpl $1, %edi
    jbe greska

    cmpl dec(, %ebx, 4), %eax
    jb post
    movb rom1(, %ebx, 1), %cl
    movb %cl, (%esi)
    incl %esi
    decl %edi
    movb rom2(, %ebx, 1), %cl
    cmpb $' ', %cl
    je oduzmi
    cmpl $1, %edi
    jbe greska
    movb %cl, (%esi)
    incl %esi
    decl %edi
oduzmi:
    subl dec(, %ebx, 4), %eax
    jmp konvertuj
post:
    incl %ebx
    jmp konvertuj

greska:
    incl -4(%ebp)
    jmp kraj

kraj:
    movb $0, (%esi)
    popl %ebx
    popl %edi
    popl %esi
    movl -4(%ebp), %eax
    movl %ebp, %esp
    popl %ebp
    ret




# unsigned int inter_to_oct_str(unsigned int broj, char* str, unsigned int duzina);
.section .text
.globl inter_to_oct_str
inter_to_oct_str:
    