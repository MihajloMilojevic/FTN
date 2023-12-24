.section .data
	poruka_unos: .ascii "Unesite jednacinu: "
	poruka_unos_len = . - poruka_unos
	poruka_resenje: .ascii "Resenje: x = "
	poruka_resenje_len = . - poruka_resenje
	poruka_greska_operacija: .ascii "Greska! Neispravna operacija!\n"
	poruka_greska_operacija_len = . - poruka_greska_operacija
	poruka_greska_konverzija: .ascii "Greska pri konverziji!\n"
	poruka_greska_konverzija_len = . - poruka_greska_konverzija
	
	max_unos = 100
	unos: .fill max_unos, 1, 42
	baza: .long 10
	broj_str: .fill max_unos, 1, 42
	prvi_broj: .long 0
	drugi_broj: .long 0
	greska: .long 0
	operacija: .fill 1, 1, 42
	rezultat: .long 0
	rezultat_str: .fill max_unos, 1, 42
	rezultat_len: .long 0
	
.section .text
.globl main

# konverzija stringa u broj (engl. string to integer conversion)
# int (char* str, int baza, int *greska)
str_to_int:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	
	movl 8(%ebp), %esi
	movl 12(%ebp), %ebx
	xorl %eax, %eax
	xorl %edx, %edx
	xorl %ecx, %ecx
	
str_to_int_petlja:
	movb (%esi), %cl
	cmpb $0, %cl
	je kraj_str_to_int
	subb $'0', %cl
	js str_to_int_greska
	cmpb %bl, %cl
	jae str_to_int_greska
	mull %ebx
	addl %ecx, %eax
	incl %esi
	jmp str_to_int_petlja
	
str_to_int_greska:
	movl 16(%ebp), %esi
	movl $1, (%esi)
	
kraj_str_to_int:
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
	
# konverzija broja u string (engl. integer to string conversion)
# greška nije neophodna kao parametar (engl. the third parameter "greska" (error) is not required)
# dužina stringa vraća se kroz eax (engl. the length of the string is returned through the eax register)
# int (char* str, int broj, int* greska, int baza)
int_to_str:	
	pushl %ebp
	movl %esp, %ebp
	pushl %esi
	pushl %edi
	pushl %ebx
	
	movl 8(%ebp), %esi
	movl %esi, %edi
	movl 12(%ebp), %eax
	
	movl 20(%ebp), %ebx
	xorl %edx, %edx
	xorl %ecx, %ecx
	
petlja_int_to_str:
	xorl %edx, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%esi)
	incl %ecx
	cmpl $0, %eax
	je kraj_deljenja_int_to_str
	incl %esi
	jmp petlja_int_to_str
	
kraj_deljenja_int_to_str:
	incl %esi
	movb $'\n', (%esi)
	incl %ecx
	decl %esi
	
obrni_int_to_str:
	cmpl %esi, %edi
	jae kraj_int_to_str
	movb (%esi), %dl
	movb (%edi), %dh
	movb %dh, (%esi)
	movb %dl, (%edi)
	incl %edi
	decl %esi
	jmp obrni_int_to_str
	
kraj_int_to_str:
	movl %ecx, %eax
	popl %ebx
	popl %edi
	popl %esi
	movl %ebp, %esp
	popl %ebp
	ret
	
main:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_unos, %ecx
	movl $poruka_unos_len, %edx
	int $0x80
	
	movl $3, %eax
	movl $0, %ebx
	movl $unos, %ecx
	movl $max_unos, %edx
	int $0x80
	
	movl $broj_str, %edi
	movl $unos, %esi
	
# traženje razmaka, odnosno granice prvog broja (engl. search for a space, that is, the delimiter for the first number)
# nađeni broj se kao string smešta u "broj_str" promenljivu (engl. the characters of the first number are placed in the "broj_str" variable)
trazi_prvi_broj:
	cmpb $' ', (%esi)
	je nadjen_prvi_broj
	movb (%esi), %bl
	movb %bl, (%edi)
	incl %esi
	incl %edi
	jmp trazi_prvi_broj
	
nadjen_prvi_broj:
	movb $0, (%edi) # dodavanje \0 na kraj izvučenog broja (engl. add a \0 to the end of the extracted number)
	
	# konvertuj prvi broj (engl. convert the first number)
	pushl $greska
	pushl baza
	pushl $broj_str
	call str_to_int
	addl $12, %esp
	
	# proveri grešku (engl. check for error)
	cmpl $0, greska
	jne greska_konverzija
	
	# smesti izračunati broj u promenljivu "prvi_broj" (engl. move the first number to the "prvi_broj" variable)
	movl %eax, prvi_broj
	
	# uveća se esi da se sa razmaka pređe na opreaciju (engl. increment esi to point to the operation character)
	incl %esi
	movb (%esi), %bl
	movb %bl, operacija
	
	addl $6, %esi # broj sa desne strane jednakosti je uvek 6 mesta dalje od operacije 
		      # (engl. the number on the right side of '=' is always 6 places away from the operation character)
	movl $broj_str, %edi
	
# traži se broj sa desne strane jednakosti, čiji je kraj \n, i smešta se u "broj_str"
# (engl. search for the number on the right side of '=', which ends with a \n, and place its characters in "broj_str")
trazi_drugi_broj:
	cmpb $'\n', (%esi)
	je nadjen_drugi_broj
	movb (%esi), %bl
	movb %bl, (%edi)
	incl %esi
	incl %edi
	jmp trazi_drugi_broj
	
nadjen_drugi_broj:
	movb $0, (%edi) # dodavanje \0 na kraj izvučenog broja (engl. add a \0 to the end of the extracted number)
	
	# konvertuj prvi broj (engl. convert the first number)
	pushl $greska
	pushl baza
	pushl $broj_str
	call str_to_int
	addl $12, %esp
	
	# proveri grešku (engl. check for error)
	cmpl $0, greska
	jne greska_konverzija
	
	# smesti izračunati broj u promenljivu "drugi_broj" (engl. move the number to the "drugi_broj" variable)
	movl %eax, drugi_broj
	
	# proveri operaciju (engl. check the operation)
	cmpb $'-', operacija
	je minus
	cmpb $'+', operacija
	jne greska_operacija # skoči na grešku ako nije ni plus ni minus (engl. jump to error handling if its neither a plus, nor a minus)
	
	# računanje rezultat ako je u pitanju plus (engl. result calculation if the operation is a plus)
	movl drugi_broj, %eax
	subl prvi_broj, %eax
	movl %eax, rezultat
	jmp konvertuj_u_string
	
# računanje rezultat ako je u pitanju minus (engl. result calculation if the operation is a minus)
minus:
	movl prvi_broj, %eax
	subl drugi_broj, %eax
	movl %eax, rezultat

konvertuj_u_string:

	# konvertuj rezultat u string (engl. convert the result to a string)
	pushl baza
	pushl $greska
	pushl rezultat
	pushl $rezultat_str
	call int_to_str
	addl $16, %esp
	movl %eax, rezultat_len

	# ispis krajnje poruke (engl. output the final message)
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_resenje, %ecx
	movl $poruka_resenje_len, %edx
	int $0x80
	
	# ispis rezultata (engl. output the result)
	movl $4, %eax
	movl $1, %ebx
	movl $rezultat_str, %ecx
	movl rezultat_len, %edx
	int $0x80
	
	jmp kraj
	
# greška pri konverziji (engl. conversion error)
greska_konverzija:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_greska_konverzija, %ecx
	movl $poruka_greska_konverzija_len, %edx
	int $0x80
	jmp kraj
	movl $1, greska
		
# greška u operaciji (engl. operation character error)
greska_operacija:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_greska_operacija, %ecx
	movl $poruka_greska_operacija_len, %edx
	int $0x80
	movl $2, greska
	
kraj:
	movl $1, %eax
	movl greska, %ebx
	int $0x80
	
	
	
	

	
	 
	
	
	
	
	
	
