# Opis: Funkcija koja sabira dva niza
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 12.11.2023.
#                    +8               +12           +16     +20
# int saberi_niz(long long *a, long long *b, long long *c, int n);
.section .text
.globl saberi_niz

saberi_niz:
    pushl %ebp
    movl %esp, %ebp             #                           -4        -8  
    subl $8, %esp              # 4 lokalne promenjlive a[i] nizi, b[i] nizi
    pushl %ebx
    pushl %esi
    

    cmpl $1, 20(%ebp)
    jl greska                   # n < 1

    movl $0, %esi               # index = 0

petlja:
    cmpl %esi, 20(%ebp)
    je ok                       # i < n

    movl 8(%ebp), %eax          # adresa a
    movl 12(%ebp), %ebx          # adresa b

    movl (%eax, %esi, 8), %ecx           # u ecx se nalaze nizi bitovi a[i]
    movl 4(%eax, %esi, 8), %edx           # u edx se nalaze visi bitovi a[i]
    addl (%ebx, %esi, 8), %ecx
    adcl 4(%ebx, %esi, 8), %edx
    jo greska
    
    # rez
    movl 16(%ebp), %eax          # adresa c
    movl %ecx, (%eax, %esi, 8)
    movl %edx, 4(%eax, %esi, 8)

    incl %esi
    jmp petlja

greska:
    movl $1, %eax
    jmp kraj

ok:
    movl $0, %eax
kraj:
    popl %esi
    popl %ebx
    movl %ebp, %esp         # obrisi lokalne promenljive
    popl %ebp               # restauriraj base pointer
    ret


