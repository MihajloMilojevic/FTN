.section .data
a: .quad 0x8000
b: .long 0x8001,1
greska: .byte 0
.section .text
.globl main
main:
movb $0, greska
movl a, %eax
addl b, %eax
movl a+4, %edx
adcl b+4, %edx
jnc kraj
incb greska
kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
