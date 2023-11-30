# autor Mihajlo Milojevic SV57-2023
# unsigned int Zadatak(unsigned int l, unsigned int r);

.section .text
.global Zadatak
Zadatak:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx
    pushl %esi

    movl $0, %eax       # rezultat 
    movl $1, %ebx       # maska
    movl 12(%ebp), %ecx     # broj nula sa desne strane
    shll %cl, %ebx      # shiftujemo masku da bude na r+1 bitu sa desne strane
    movl %ecx, %esi     # r korisistimo kao pocetnu vrednost brojaca
    movl $32, %edx
    subl 8(%ebp), %edx        # edx sadrzi index prvog bita koji je nula posle jedinica 

petlja:
    cmpl %esi, %edx
    je return
    orl %ebx, %eax
    shll $1, %ebx
    incl %esi
    jmp petlja

return:
    popl %esi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret