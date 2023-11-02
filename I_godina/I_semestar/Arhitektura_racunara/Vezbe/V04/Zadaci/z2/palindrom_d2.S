#Opis: Proverava da li je uneti string palindrom 
#Treba voditi racuna i o velicini slova i drugim znacima
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 2.11.2023

.section .data
poruka: .ascii "Unesite string:\0"
n_p = . - poruka

nijep:  .ascii "String nije palindrom.\n\0"
n_n = . - nijep

jestep: .ascii "String je palindrom.\n\0"
n_j = . - jestep

unos:   .fill 50,1,42
n_u = . - unos
duz_pal: .long 0


.section .text
.globl main

main:

    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal poruka, %ecx
    movl $n_p, %edx
    int $0x80

    # unesi pal
    movl $3, %eax
    movl $0, %ebx
    leal unos, %ecx
    movl $n_u, %edx
    int $0x80

    movl %eax, duz_pal

uppercase:
    # prolazak kroz string
    movl $0, %esi
uslov_upper:
    cmpb $10, unos(, %esi, 1)
    je provera_palindroma
    movb unos(, %esi, 1), %al   # trenutni char
    cmpb $'a', %al
    jb post_uppper
    cmpb $'z', %al
    ja post_uppper
    subb $32, %al
    movb %al, unos(, %esi, 1)

post_uppper:
    incl %esi
    jmp uslov_upper

provera_palindroma:
    movl $0, %esi
    movl duz_pal, %edi
    subl $2, %edi           # poslednji karakter ima index n-1 i jos \n -1 pa -2

uslov_pal:
    cmpl %esi, %edi
    jb jeste
    movb unos(, %esi, 1), %al
    movb unos(, %edi, 1), %ah
    # proveri da je levi slovo
    cmpb $'A', %al
    jb nije_l
    cmpb $'Z', %al
    ja nije_l

    # proveri da je desno slovo
    cmpb $'A', %ah
    jb nije_d
    cmpb $'Z', %ah
    ja nije_d

    cmpb %ah, %al
    jne nije
    jmp post_pal
nije_l:
    incl %esi
    jmp uslov_pal

nije_d:
    decl %edi
    jmp uslov_pal
post_pal:
    incl %esi
    decl %edi
    jmp uslov_pal
    

nije:
    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal nijep, %ecx
    movl $n_n, %edx
    int $0x80

    movl $1, %eax
    movl $1, %ebx
    int $0x80

jeste:
    # ispisi poruku
    movl $4, %eax
    movl $1, %ebx
    leal jestep, %ecx
    movl $n_j, %edx
    int $0x80

    movl $1, %eax
    movl $0, %ebx
    int $0x80






