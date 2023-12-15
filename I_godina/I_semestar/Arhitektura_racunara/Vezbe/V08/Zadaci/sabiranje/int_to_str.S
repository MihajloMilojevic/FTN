# autor: Mihajlo Milojevic SV57/2023
# datum: 7.12.2023.

# unsigned int int_to_str(unsigned int broj, char* str, unsigned int duzina, unsigned int baza, unsigned int *int_to_str_greska);
.section .text
.globl int_to_str
int_to_str:
    pushl %ebp
    movl %esp, %ebp
    pushl $0     # int_to_str_greska
    pushl $0     # duzina
    pushl %esi
    pushl %edi
    pushl %ebx

    movl 8(%ebp), %eax      # broj
    movl 20(%ebp), %ebx           # baza
    movl 12(%ebp), %esi     # adresa trenutnog karaktera
    movl 16(%ebp), %edi     # preostala duzina bafera

int_to_str_konvertuj:
    cmpl $1, %edi
    jbe int_to_str_greska
    xorl %edx, %edx
    divl %ebx
    cmpb $9, %dl
    ja int_to_str_slovo
int_to_str_cifra:
    addb $'0', %dl
    jmp int_to_str_nastavak
int_to_str_slovo:
    subb $10, %dl
    addb $'a', %dl

int_to_str_nastavak:
    movb %dl, (%esi)
    incl %esi
    incl -8(%ebp)
    decl %edi
    cmpl $0, %eax
    jne int_to_str_konvertuj
    movb $0, (%esi)             # \0 na int_to_str_kraj stringa
    decl %esi                   # vrati pokazivac na poslednji karakter u stringu
    movl 12(%ebp), %edi         # adresa prvog karaktera
int_to_str_obrni:
    cmpl %edi, %esi
    jbe int_to_str_kraj
    movb (%esi), %al
    movb (%edi), %ah
    movb %ah, (%esi)
    movb %al, (%edi)
    incl %edi
    decl %esi
    jmp int_to_str_obrni


int_to_str_greska:
    incl -4(%ebp)
    jmp int_to_str_kraj

int_to_str_kraj:

    movl 24(%ebp), %eax
    movl -4(%ebp), %ebx
    movl %ebx, (%eax)
    movl -8(%ebp), %eax
    popl %ebx
    popl %edi
    popl %esi
    movl %ebp, %esp
    popl %ebp
    ret