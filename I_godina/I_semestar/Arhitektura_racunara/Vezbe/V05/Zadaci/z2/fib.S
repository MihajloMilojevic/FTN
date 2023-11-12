# Opis: Funkcija koja rekurzivno racuna n-ti fibonacijev broj
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 12.11.2023.

# unsigned int fibonaci(int n, int *g);
.section .text
.globl fibonaci
.macro proveri err
    movl 12(%ebp), %ecx
    movl (%ecx), %ecx
    cmpl $0, %ecx
    jne \err
.endm

fibonaci:
    pushl %ebp
    movl %esp, %ebp
    subl $8, %esp               # lokalne promenljive za f(n-1) i f(n-2)

    movl 8(%ebp), %edx          # n
    cmpl $1, %edx
    jl greska                   # n < 1
    je osnovni                  # n = 1 - base case
    cmpl $2, %edx
    je osnovni                  # n = 2 - base case

    decl %edx                   # n--
    pushl 12(%ebp)
    pushl %edx                  
    call fibonaci               # eax = f(n-1)
    addl $8, %esp
    movl %eax, -4(%ebp)
    proveri greska

    movl 8(%ebp), %edx
    subl $2, %edx                   # n--
    pushl 12(%ebp)
    pushl %edx                  
    call fibonaci               # eax = f(n-2)
    addl $8, %esp
    movl %eax, -8(%ebp)
    proveri greska
    
    movl -8(%ebp), %eax
    addl -4(%ebp), %eax
    jc greska
    jmp ok

osnovni:
    movl $1, %eax
    jmp ok

greska:
    movl 12(%ebp), %eax
    movl $1, (%eax)
    movl $0, %eax
    jmp kraj

ok:
    movl 12(%ebp), %ecx
    movl $0, (%ecx)
kraj:
    movl %ebp, %esp         # obrisi lokalne promenljive
    popl %ebp               # restauriraj base pointer
    ret


