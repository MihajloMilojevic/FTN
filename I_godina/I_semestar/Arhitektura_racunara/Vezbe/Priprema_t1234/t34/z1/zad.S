#autor: Mihajlo Milojevic SV57-2023
#				 + 8					+ 12
# int BitSwitch(unsigned int* vrednost, int n);
.section .text
.globl BitSwitch

BitSwitch:
	pushl %ebp
	movl %esp, %ebp
	pushl %esi
	pushl %edi
	
	movl $0, %ecx
	 
	# ako je n = 0 samo izadji
	cmpl $0, 12(%ebp)	
	je kraj
	
priprema:
	movl $0, %esi
	movl 8(%ebp), %eax	# adresa prvog elementa
	
spoljasnja:
	cmpl %esi, 12(%ebp)
	je kraj
	
	movl $1, %edx	# maska
unutrasnja:
	cmpl $0x80000000, %edx
	je spoljasnja_post
	testl %edx, (%eax)
	jz unutrasnja_post
	shll $1, %edx
	xorl %edx, (%eax)
	incl %ecx
	jmp unutrasnja
	
unutrasnja_post:
	shll $1, %edx
	jmp unutrasnja
	
spoljasnja_post: 
	incl %esi
	addl $4, %eax	# na sledeci element
	jmp spoljasnja
	
kraj:
	popl %edi
	popl %esi
	movl %ebp, %esp
	popl %ebp
	movl %ecx, %eax
	ret
