#Opis: Pronalazi min i max elemente niza
#Autor: Mihajlo Milojevic SV57/2023
#Datum: 26.10.2023.

.section .data
N = 10
niz: .long 5, 6, 7, 10, 9, 1, 3, 2, 4, 8
min: .long 0
max: .long 0
.section .text
.globl main
main:
    # postavlja min i max na prvi element niza i index na 1
    movl niz, %eax          
    movl %eax, min         
    movl %eax, max          
    movl $1, %esi                # trenutni index
petlja:                         
    movl niz(, %esi, 4), %eax   # trenutni element se nalazi u eax
if_min:                         # slucaj kad je trenutni manji od min
    cmpl min, %eax          
    jge if_max              # trenutni > min ==> idi dalje, min ostaje
    movl %eax, min  
if_max:
    cmpl max, %eax          
    jle uslov              # trenutni > min ==> idi dalje, min ostaje
    movl %eax, max
uslov: 
    incl %esi
    cmpl $N, %esi         # proverava trenutni index sa N 
    jb petlja            # izvrsava petlju dokle god je index < N


kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

