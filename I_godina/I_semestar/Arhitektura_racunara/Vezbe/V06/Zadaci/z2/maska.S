# Opis: Potprogram koji kreira masku gde je n-ti bit postavljen na v, a su ostali !v. Broj je 64-bitni
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 16.11.2023
# unsigned long long maska64(unsigned int n, unsigned int v);
.section .text
.globl maska64
maska64:
	pushl %ebp
	movl %esp, %ebp
    # n > 63
    cmpl $63, 8(%ebp)
    ja nula
    # v > 1
    cmpl $1, 12(%ebp)
    ja nula
    # maska = 1
    movl $1, %eax
    movl $0, %edx
    # ecx = n
    movl 8(%ebp), %ecx
    # ako je n iz [32, 63], transliraj ga u [0, 31]
    cmpl $31, %ecx
    jbe petlja
    subl $32, %ecx
petlja:
	#while n > 0 - petlja koja dovodi 1 na n-ti bit
	cmpl $0, %ecx
	je reg_check
	shl $1, %eax
	decl %ecx
	jmp petlja
reg_check:
	# ako je n > 31 to znaci da se cifra v nalazi u registru edx
	cmpl $31, 8(%ebp)
	jna inv
	xchgl %eax, %edx
inv: 
	# maska na n-tom bitu ima 1, sto je ok ako je v = 1
	# ako je v = 0 treba invertovati sve bitove
	cmpl $1, 12(%ebp)
	je kraj
	notl %eax
	notl %edx
	jmp kraj
# greska
nula:
	movl $0, %eax
	movl $0, %edx
	jmp kraj
kraj:
    movl %ebp, %esp
    popl %ebp
    ret


