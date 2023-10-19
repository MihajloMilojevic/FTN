#Pristup elementima niza
#Petar

.section .data
niz: .long -3, 6, 7, 4, 12
.section .text
.globl main
main:
	movl $2, %eax
	movl niz(, %eax, 4), %ebx
	
	movl $niz, %eax
	addl $8, %eax
	movl (%eax), %ebx
	
	movl $niz, %ecx
	movl $2, %eax
	movl (%ecx, %eax, 4), %ebx
	
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
