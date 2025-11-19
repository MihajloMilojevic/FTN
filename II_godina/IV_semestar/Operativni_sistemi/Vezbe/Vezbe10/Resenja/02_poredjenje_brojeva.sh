#!/bin/bash

# Napisati bash skript koji za dva zadata cela broja a i b poredi 
# njihove vrednosti i ispisuje na standardni izlaz u kakvoj su relaciji.
# a i b zadati kao prizvoljne promenljive skripta sa predefinisanim
# vrednostima (npr. a=010 i b=10).
#
# Primer koriscenja:
#   ./02_poredjenje_brojeva.sh


a=010
b=10

[[ $a -gt $b ]] && echo 'a je vece od b'
[[ $a -le $b ]] && echo 'b je vece od a' || echo 'a i b su jednaki'
