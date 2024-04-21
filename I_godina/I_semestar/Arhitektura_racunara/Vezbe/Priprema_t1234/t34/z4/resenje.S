# autor: Imenko Prezimić INDEX ra1234-2023
# int prebrojNajviseUzastopnih(unsigned long long* vrednost)
.section .text
.global prebrojNajviseUzastopnih
prebrojNajviseUzastopnih:
	pushl %ebp
	movl %esp, %ebp
	
	pushl %ebx
	pushl %esi
	pushl %edi

	movl $1, %esi		# maska nizih
	xorl %edi, %edi		# maska visih
	xorl %ecx, %ecx 	# brojac trenutnog broja nula
	movl 8(%ebp), %ebx	# adresa broja

	movl (%ebx), %eax	# nizi deo
	movl 4(%ebx), %edx	# visi deo
	xorl %ebx, %ebx 	# maksimalan broj nula
proveri_kraj:
	andl %esi, %esi		# da li je esi 0? 
	jnz broji
	andl %edi, %edi		# da li je edi 0?
	jz proveri_brojac	# kada zavrsimo sa visim delom, mozda imamo novi maksimum, proveravamo to
# proverava da li smo naisli na jedinicu i visem ili nizem delu,
# ako jesmo proveravamo da li imamo novi maksimum, u suprotnom uvecava broj nula
broji:	
	testl %esi, %eax		
	jnz proveri_brojac
	testl %edi, %edx
	jnz proveri_brojac
	incl %ecx			# uvecaj broj nula
pomeri_masku:
	shll $1, %esi		# nizi se shiftuju
	rcll $1, %edi 		# za vise mora rcl da bi se uhvatio carry iz nizeg dela kada ispadne
	jmp proveri_kraj
proveri_brojac:
	cmpl %ebx, %ecx
	jbe resetuj_brojac
	movl %ecx, %ebx		# pronadjen novi maksimum
resetuj_brojac:
	xorl %ecx, %ecx		# resetuj broj nula
	andl %esi, %esi		# ako esi nije nula, i dalje smo u nizem delu, nije kraj
	jnz pomeri_masku
	andl %edi, %edi		# ako edi nije nula, i dalje smo u visem delu, nije kraj
	jnz pomeri_masku	# ako su oba nula znaci da smo prosli kroz citav broj
kraj:					# ako smo dosli dovde, i esi i edi su bili nula, prosli smo kroz citav broj
	movl %ebx, %eax		# povratna vrednost mora ici u eax
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
