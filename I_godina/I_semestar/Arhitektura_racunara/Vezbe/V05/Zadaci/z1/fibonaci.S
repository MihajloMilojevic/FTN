#Opis: Potprogram koji racuna n-ti element fibonacijevog niza
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 9.11.2023.
.section .text
.globl fibonaci
# int fibonaci(int n +4, unsigned int* rez +8);
fibonaci:
    pushl %ebp
    movl %esp, %ebp

    cmpl $1, 8(%ebp)
    jl error
    je base_case

    cmpl $2, 8(%ebp)
    je base_case
    movl $1, %eax   # [i - 2] pre pre
    movl $1, %ecx   # [i - 1] pre
                    # %edx cuva trenutni
    movl $2, %esi   # tr index - i

petlja:
    cmpl %esi, 8(%ebp)      # while i < n
    je print
    movl %ecx, %edx         # tr = pr
    add %eax, %edx          # tr += pr_pr
    jc error
    incl %esi
    movl %ecx, %eax
    movl %edx, %ecx
    jmp petlja

print:
    movl 12(%ebp), %eax
    movl %edx, (%eax)
    movl $0, %eax
    jmp kraj
base_case: 
    movl 12(%ebp), %eax
    movl $1, (%eax)
    movl $0, %eax
    jmp kraj
error:
    movl $1, %eax
    jmp kraj
kraj:
    movl %ebp, %esp
    popl %ebp
    ret