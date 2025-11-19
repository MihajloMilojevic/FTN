#!/bin/bash

# Napisati bash skript koji prima N argumenata komandne linije i na
# standardni izlaz ispisuje koliko je argumenata prosledjeno i svaki
# od argumenata u novoj liniji.
#
# Primer poziva:
#   ./03_argumenti


echo "Skriptu je prosledjeno $# argumenata komandne linije i to su:"

for arg in "$@"
do
    echo "$arg"
done
