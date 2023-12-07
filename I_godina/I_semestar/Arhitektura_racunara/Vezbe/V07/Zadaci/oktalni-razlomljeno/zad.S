# autor: Mihajlo Milojevic SV57/2023
# datum: 7.12.2023.

# unsigned int inter_to_oct_str_float(unsigned int broj, char* str, unsigned int duzina);
.section .text
.globl inter_to_oct_str_float
inter_to_oct_str_float:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # greska
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl $8, %ebx           # baza
    movl $100000000, %ecx   # skalar
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera
    movl $'0', (%esi)
    incl %esi
    decl %edi
    movl $'.', (%esi)
    incl %esi
    decl %edi
    
    cmpl $1, %edi
    jbe greska

konvertuj:
    cmpl $1, %edi
    je kraj
    mull %ebx
    divl %ecx
    xchgl %eax, %edx
    addb $'0', %dl
    movb %dl, (%esi)
    incl %esi
    decl %edi
    cmpl $0, %eax
    jne konvertuj
    
    jmp kraj


greska:
    incl -4(%ebp)
    jmp kraj

kraj:
    movb $0, (%esi)             # \0 na kraj stringa
    popl %ebx
    popl %edi
    popl %esi
    movl -4(%ebp), %eax
    movl %ebp, %esp
    popl %ebp
    ret