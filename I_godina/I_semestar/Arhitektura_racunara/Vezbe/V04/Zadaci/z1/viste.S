#Opis: Unosi ime i ispisuje ga
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 2.11.2023

.section .data
poruka1: .ascii "Unesite ime i prezime: \0"
n1 = . - poruka1
poruka2: .ascii "Vi ste: \0"
n2 = . - poruka2
imeprez: .fill 50,1,42
n3 = . - imeprez
duzina_imena: .long 0

malo_a = 'a'
malo_z = 'z'

.section .text
.globl main
main:
unos:
    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal poruka1, %ecx
    movl $n1, %edx
    int $0x80

    # unesi ime
    movl $3, %eax
    movl $0, %ebx
    leal imeprez, %ecx
    movl $n3, %edx
    int $0x80

    movl %eax, duzina_imena

    # prolazak kroz ime
    movl $0, %esi
uslov:
    cmpb $10, imeprez(, %esi, 1)
    je ispis
    movb imeprez(, %esi, 1), %al   # trenutni char
    cmpb $malo_a, %al
    jb post
    cmpb $malo_z, %al
    ja post
    subb $32, %al
    movb %al, imeprez(, %esi, 1)

post:
    incl %esi
    jmp uslov

    
ispis:
    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal poruka2, %ecx
    movl $n2, %edx
    int $0x80

    # ispisi ime
    movl $4, %eax
    movl $1, %ebx
    leal imeprez, %ecx
    movl duzina_imena, %edx
    int $0x80



    jmp kraj
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


