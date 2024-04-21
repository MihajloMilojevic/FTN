#autor: Imenko Prezimić INDEX ra1234-2015

.section .data
	ulaz_poruka: .ascii "Unesite string: \0"
	ulaz_poruka_len = . - ulaz_poruka
	
	ulaz_max = 30	
	ulaz: .fill ulaz_max, 1, 42
	
	prev_digit: .byte '0'   # promenljiva koja čuva prethodno obrađenu cifru
				# postavlja se na cifru 0 kako bi bilo koja
				# cifra na koju se prvo naiđe u strignu bila
				# veća od prev_digit; time se obezbedi da 
				# prva operacija uvek bude množenje
				
	povratna_vrednost: .long 0
.section .text
.globl main
main:	
	
	# ispis poruke
	movl $4, %eax
	movl $1, %ebx	
	leal ulaz_poruka, %ecx
	movl $ulaz_poruka_len, %edx
	int $0x80

	# unos stringa
	movl $3, %eax
	movl $0, %ebx	
	leal ulaz, %ecx
	movl $ulaz_max, %edx
	int $0x80
	
	
	movl $1, %eax   # čuvaće rezultat; pogodno jer eax svakako čuva rezultat 
			# i množenja i deljenja; postavlja se na 1 jer će prva
			# operacija biti množenje, a 1 je neutralni element
			# za množenje
			
	movl $ulaz, %esi   # čuva adresu trenutnog karaktera zarad indirektnog adresiranja  
	
	movl $0, %ebx   # bl će se koristiti za čuvanje karaktera, ali želimo da množenje i 
			# deljenje bude 32-bitno; zbog toga se ebx postavlja na nula
			# niži bitovi (%bl) čuvaju karakter, a viši se anuliraju da ne bi
			# uticali na rezultat pri množenju i deljenju sa celim %ebx 
	
petlja:
	cmpb $'\n', (%esi)   # uslov izlaska iz petlje je nailazak na karakter za novi red
	je kraj_petlja
	
	
	movb (%esi), %bl   # trenutni karakter u %bl
	
	# ispituje se da li je karakter u opsegu cifara,
	# isključujući cifru 0
	cmpb $'1', %bl    
	jb dalje
	cmpb $'9', %bl
	ja dalje
	
	# ako je trenutna cifra veća od prethodne
	# idi na množenje
	cmpb prev_digit, %bl
	ja mnozi
	
	# ako trenutna cifra nije veća od prethodne (manja je ili jednaka),
	# izvrši deljenje
	movb %bl, prev_digit   # trenutna cifra postaje prethodna
	movl $0, %edx   # anuliraj viši deo za deljenje; ne koristi se
	divl %ebx
	
	cmpl $0, %edx   # proveri ostatak
	je prekini_izvrsavanje_deljenje   # ako je nula, prekini sa petljom
	jmp dalje
	
mnozi:
	movb %bl, prev_digit   # trenutna cifra postaje prethodna
	mull %ebx
	
	jc prekini_izvrsavanje_mnozenje   # ako je došlo do prekoračenje, prekini sa petljom
	
dalje:
	incl %esi   # pređi na sledeći karakter
	jmp petlja
	
kraj_petlja:
	movl $0, %edx   
	movl $128, %ebx   # ako je prekinuta petlja, deli sa 256 (mora se 256
			  # smestiti u registar, ne može se proslediti div
			  # instrukciji kao konstanta)
	divl %ebx
	movl %edx, povratna_vrednost   # ostatak pri deljenju (%edx) postaje povratna vrednost
	jmp kraj
	
prekini_izvrsavanje_deljenje:
	movl $45, povratna_vrednost   # vrati 45 ako je prekinuto izvršavanje zbog deljenja
	jmp kraj
	
prekini_izvrsavanje_mnozenje:
	movl $54, povratna_vrednost   # vrati 54 ako je prekinuto izvršavanje zbog množenja
	
kraj:
	movl $1, %eax
	movl povratna_vrednost, %ebx
	int $0x80

