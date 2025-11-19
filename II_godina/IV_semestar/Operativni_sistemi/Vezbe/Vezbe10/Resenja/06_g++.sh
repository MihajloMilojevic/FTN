#!/bin/bash

# Napisati bash skript za kompajliranje svih cpp datoteka u okviru zadatog direktorijuma.
# Direktorijum se zadaje kao argument komandne linije. Za svaku izvornu datoteku kompajler
# generise izvrsnu datoteku naziva koji odgovara nazivu izvorne datoteke bez ekstenzije
# (videti komandu basename). Na primer, ako je izvorna datoteka helloworld.cpp,
# generisana izvrsna datoteka treba da se zove helloworld. Za svaku izvornu datoteku koju
# kompajlira, skript na standardni izlaz ispisuje da li je kompajliranje bilo uspesno ili ne.
# Standardni izlaz i standardni izlaz greške g++ komande preusmeriti u datoteku compile.log.
#
# Napomene:
#   - Svaku datoteku prilozenu uz zadatak je moguce kompajlirati komandom 
#       g++ <dat.cpp> -o <dat>
#   - Implementirati provere ispravnosti zadatog direktorijuma (da li postoji, da li
#     korisnik koji pokrece skript ima prava citanja/pisanja za taj direktorijum)
#   - U zadatom direktorijumu ne moraju biti samo cpp datoteke
#
# Argumenti:
#   $1 - putanja do direktorijuma u kojem se nalaze datoteke za kompajliranje
# 
# Primer poziva:
#   ./06_g++.sh 06_izvorni_kodovi/


tdir=$1

if [ ! -d $tdir ]; then
    echo "Greska. $tdir nije direktorijum."
elif [ ! -r $tdir ]; then
    echo "Greska. Korisnik nema pravo citanja $tdir direktorijum."
elif [ ! -w $tdir ]; then
    echo "Greska. Korisnik nema pravo pisanja u $tdir direktorijum."
else
    cd $tdir;
    for d in $(ls *.cpp); do
        g++ $d -o $(basename $d .cpp) -pthread 1>&2 2>compile.log;

        success=$?
        if [[ $success -eq 0 ]]; then
            echo "Datoteka $d je uspesno kompajlirana."
        else
            echo "Greska pri kompaliranju datoteke $d."
        fi
    done
fi

