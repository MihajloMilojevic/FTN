#program racuna NZD
#autor: Imenko Prezimic e12345
.section .data
.section .text
.globl main
main:
       movl $12,%eax    #12->eax
       movl $8,%ebx     #8->ebx
uporedi:
       cmpl %ebx,%eax
       je kraj          #skok ako eax=ebx
       cmpl %ebx,%eax
       ja vece          #skok ako eax>ebx
       subl %eax,%ebx   #ebx-eax->ebx
       jmp uporedi
vece:
       subl %ebx,%eax 	#eax-ebx->eax
       jmp uporedi
kraj:
       movl $1, %eax
       movl $0, %ebx
       int $0x80


