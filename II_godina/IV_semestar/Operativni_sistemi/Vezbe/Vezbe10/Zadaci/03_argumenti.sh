#!/bin/bash
#
# Napisati bash skript koji prima N argumenata komandne linije i na
# standardni izlaz ispisuje koliko je argumenata prosledjeno i svaki
# od argumenata u novoj liniji.
#
# Primer poziva:
#   ./03_argumenti


# TODO implementirati
echo $#
for (( i = 1 ; $i <= $# ; i++ ))
do
    echo "${!i}"
done
