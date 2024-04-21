# autor: Imenko Prezimić INDEX ra1234-2023
#int prebrojPalindrome(unsigned long long *niz, int n)

.section .text
.globl prebrojPalindrome
prebrojPalindrome:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	
	movl 8(%ebp), %eax	# adresa niza
	movl $0, %ebx		# indeks
	
	movl $0x80000000, %edi	# maska za pocetak broja
	movl $1, %esi		# maska za kraj broja 
	
	movl $0, %ecx		# brojac palindroma
	
petlja:	
	cmpl 12(%ebp), %ebx
	je kraj

	testl %esi, (%eax, %ebx, 8)
	jz nula_nizi
	jnz jedan_nizi
	
nula_nizi:
	testl %edi, 4(%eax, %ebx, 8)
	jz dalje
	jmp sledeci_element		# nije palindrom	
	
jedan_nizi:
	testl %edi, 4(%eax, %ebx, 8)
	jnz dalje
	jmp sledeci_element		# nije palindrom
	
dalje:
	shll $1, %esi
	jc palindrom
	shrl $1, %edi
	jc palindrom
	jmp petlja
	
palindrom:
	incl %ecx
	jmp sledeci_element
	
sledeci_element:
	incl %ebx
	movl $0x80000000, %edi
	movl $1, %esi
	jmp petlja
	
kraj:
	movl %ecx, %eax
	
	popl %edi
	popl %esi
	popl %ebx	
	movl %ebp, %esp
	popl %ebp
	ret
