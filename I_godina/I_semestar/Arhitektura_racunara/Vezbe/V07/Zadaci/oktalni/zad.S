# autor: Mihajlo Milojevic SV57/2023
# datum: 7.12.2023.

# unsigned int inter_to_oct_str(unsigned int broj, char* str, unsigned int duzina);
.section .text
.globl inter_to_oct_str
inter_to_oct_str:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # greska
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl $8, %ebx           # baza
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera

konvertuj:
    cmpl $1, %edi
    jbe greska
    xorl %edx, %edx
    divl %ebx
    addb $'0', %dl
    movb %dl, (%esi)
    incl %esi
    decl %edi
    cmpl $0, %eax
    jne konvertuj
    movb $0, (%esi)             # \0 na kraj stringa
    decl %esi                   # vrati pokazivac na poslednji karakter u stringu
    movl 12(%ebp), %edi         # adresa prvog karaktera
obrni:
    cmpl %edi, %esi
    jbe kraj
    movb (%esi), %al
    movb (%edi), %ah
    movb %ah, (%esi)
    movb %al, (%edi)
    incl %edi
    decl %esi
    jmp obrni


greska:
    incl -4(%ebp)
    jmp kraj

kraj:
    popl %ebx
    popl %edi
    popl %esi
    movl -4(%ebp), %eax
    movl %ebp, %esp
    popl %ebp
    ret