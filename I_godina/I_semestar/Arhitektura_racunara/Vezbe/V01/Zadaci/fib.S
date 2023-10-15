#Opis: Program koji racuna n-ti element fibonacijevog niza
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 15.10.2023.

.section .data
.section .text
.globl main
main:
    movl $5, %eax   # n
    movl $0, %ebx   # pre pre // n-2 element
    movl $1, %ecx   # pre //n-1 element
    movl $0, %edx   # tr //n element

    cmpl $1, %eax   #slucaj n = 1 -> prvi fib broj = 0
    je n1
    cmpl $2, %eax   #slucaj n = 2 -> prvi fib broj = 0
    je n2
    
uslov: 
    cmpl $2, %eax       #while(n>2)
    je kraj

    movl %ebx, %edx     #tr = prepre
    addl %ecx, %edx     #tr += pre
                        #==> tr = prepre + pre - tr je trenutni fibonacijev broj
    
    movl %ecx, %ebx     #prepre  = pre
    movl %edx, %ecx     #pre = tr
    subl $1, %eax       #n--
    jmp uslov

n1:
    movl $0, %edx
    jmp kraj
n2:
    movl $1, %edx
    jmp kraj

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80


