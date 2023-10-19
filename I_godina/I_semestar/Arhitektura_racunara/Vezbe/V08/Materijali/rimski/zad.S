.section .text
.globl roman_to_inter
dec:    .long 1000, 500, 100, 50, 10, 5, 1
rom:   .ascii "MDCLXVI\0"

roman_to_inter:
    ret

