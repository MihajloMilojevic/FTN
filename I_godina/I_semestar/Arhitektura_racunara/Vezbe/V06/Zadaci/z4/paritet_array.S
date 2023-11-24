# Opis: Potprogram koji postavlja bit najvise vrednosti 16-bitnom broju na bit pariteta
# Autor: Mihajlo Milojevic SV57/2023
# Datum: 16.11.2023

# int SetParityArray(unsigned short int* niz, int n);
.section .text
.globl SetParityArray
SetParityArray:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx
    pushl %esi
    
    movl 8(%ebp), %eax
    movl (%eax), %edx	# edx sadrzi adresu pocetka niza
    movl $0, %ebx	# brojac jedinica
    movl $0, %esi	# brojac petlje
petlja:
	cmpl %esi, 12(%ebp) # i < n
	jz kraj
	leal (%edx, %esi, 2), %ecx 	# ecx sadrti adresu trenutnog broja
	pushl %ecx
	call SetParity
	addl $4, %esp
	addl %eax, %ebx
	incl %esi
	jmp petlja
kraj:
    popl %esi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret


