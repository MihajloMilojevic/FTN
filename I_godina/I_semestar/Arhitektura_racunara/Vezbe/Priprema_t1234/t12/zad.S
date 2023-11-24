#autor: Mihajlo Milojevic SV57-2023

.section .data
ulaz_str: .ascii "Unesite string: \0"
poruka_duz = . - ulaz_str
unos_max = 50
unos: 	.fill unos_max,1,42
duzina: .long 0
izlaz: .long 0

min: .ascii "9"
max: .ascii "0"
cifra: .long 0

.section .text
.globl main
main:
	# ispis poruke
	movl $4, %eax
	movl $1, %ebx
	movl $ulaz_str, %ecx
	movl $poruka_duz, %edx
	int $0x80
	
	# unos stringa
	movl $3, %eax
	movl $0, %ebx
	movl $unos, %ecx
	movl $unos_max, %edx
	int $0x80
	
	# cuvanje duzine strina
	movl %eax, duzina
	
	movl $0, %esi	
petlja:
	# do kraja stringa
	cmpl duzina, %esi
	je rezultat
	movb unos(, %esi), %al	# trenutni karakter
	# \n je kraj stringa
	cmpb $'\n', %al
	je rezultat
	# manje od 0 -> nije cifra
	cmpb $'0', %al
	jb post
	# vece od 9 -> nije cifra
	cmpb $'9', %al
	ja post
	movl $1, cifra	# ima cifara 
uslov_min:
	# trenutni je manji od min -> on je novi min
	cmpb min, %al
	ja uslov_max
	movb %al, min
uslov_max:
	# trenutni je veci od max -> on je novi max
	cmpb max, %al
	jb post
	movb %al, max
	
post:
	incl %esi
	jmp petlja

rezultat:	
	cmpl $0, cifra
	je kraj
	movl min, %eax
	addl max, %eax
	movl %eax, izlaz
	
kraj:
	movl $1, %eax
	movl izlaz, %ebx
	int $0x80

