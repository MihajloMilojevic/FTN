#!/bin/bash
#
# Napisati bash skript koji za dva zadata cela broja a i b poredi 
# njihove vrednosti i ispisuje na standardni izlaz u kakvoj su relaciji.
# a i b zadati kao prizvoljne promenljive skripta sa predefinisanim
# vrednostima (npr. a=100 i b=10).
#
# Primer koriscenja:
#   ./02_poredjenje_brojeva.sh


# TODO implementirati
if [ $1 -lt $2 ]
then
    echo "a is less then b"
else
    echo "a is greater then or equal to b"
fi