#autor: Mihajlo Milojevic SV57-2023
				 + 8					+ 12
# int BitSwitch(unsigned int* vrednost, int n);
.section .text
.globl BitSwitch

.macro RETURN value
	return:
	popl %edi
	popl %esi
	movl %ebp, %esp
	popl %ebp
	movl \value, %eax
	ret
.endm

.macro VAR name, pointer
	.macro \name
		\pointer
	.endm
.endm

BitSwitch:
	pushl %ebp
	movl %esp, %ebp
	subl $4, %esp
	pushl %esi
	pushl %edi
	
	VAR count, -4(%ebp)
	VAR n, 12(%ebp)
	
	movl, $0, count
	 
	# ako je n = 0 samo izadji
	cmpl $0, n	
	jne priprema
	RETURN $0
	
priprema:
	VAR i, %esi
	movl $0, i
	
spoljasnja:
	cmpl i, n
	je kraj
	VAR maska, %eax
	movl $1, maska
	VAR j, %edi
	movl $0, j
	VAR tr, %edx
	movl 8(%ebp), %eax
	
unutrasnja:
	cmpl $32, j
	je spoljasnja_post
	
unutrasnja_post:
	incl j
	jmp unutrasnja
	
spoljasnja_post: 
	incl i
	jmp spoljasnja
	
kraj:
	RETURN count
