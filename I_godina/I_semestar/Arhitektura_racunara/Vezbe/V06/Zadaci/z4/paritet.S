# Opis: Potprogram koji postavlja bit najvise vrednosti 16-bitnom broju na bit pariteta
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 16.11.2023

# int SetParity(unsigned short int* v);
.section .text
.globl SetParity
SetParity:
    pushl %ebp
    movl %esp, %ebp
    pushl %ecx
    pushl %edx
    movl 8(%ebp), %eax
    movw (%eax), %dx	# dx sadrzi broj
    movw $0, %ax 	# brojac jedinica
    movw $1, %cx	# maska
petlja:
	cmpw $0x8000, %cx		# dok maska ne prodje kroz svih 15 bitova
	je postavi
	test %cx, %dx
	jz post
	incw %ax 
post: 
	shlw $1, %cx
	jmp petlja
postavi:
	andw $1, %ax
	rorw $1, %ax
	orw %ax, %dx
	movl 8(%ebp), %eax
	movw %dx, (%eax)
	
	movl $0, %eax
	andw $0x8000, %dx
	jz kraj
	incl %eax
kraj:
    popl %edx
    popl %ecx
    movl %ebp, %esp
    popl %ebp
    ret


