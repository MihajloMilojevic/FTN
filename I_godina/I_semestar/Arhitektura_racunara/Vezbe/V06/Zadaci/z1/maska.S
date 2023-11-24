# Opis: Potprogram koji kreira masku gde je n-ti bit postavljen na v, a su ostali !v. Broj je 32-bitni
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 16.11.2023
# unsigned int maska(unsigned int n, unsigned int v);
.section .text
.globl maska
maska:
	pushl %ebp
	movl %esp, %ebp
    movl $0, %eax
    # n > 31
    cmpl $31, 8(%ebp)
    ja nula
    # v > 1
    cmpl $1, 12(%ebp)
    ja nula
    # maska = 1
    movl $1, %eax
petlja:
	#while n > 0 - petlja koja dovodi 1 na n-ti bit
	cmpl $0, 8(%ebp)
	je inv
	shl $1, %eax
	decl 8(%ebp)
	jmp petlja
inv: 
	# maska na n-tom bitu ima 1, sto je ok ako je v = 1
	# ako je v = 0 treba invertovati sve bitove
	cmpl $1, 12(%ebp)
	je kraj
	notl %eax
	jmp kraj
# greska
nula:
	movl $0, %eax
	jmp kraj
kraj:
    movl %ebp, %esp
    popl %ebp
    ret


