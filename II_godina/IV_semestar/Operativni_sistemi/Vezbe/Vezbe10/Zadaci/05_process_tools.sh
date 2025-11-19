#!/bin/bash
#
# Osnovni deo zadatka:
# Napisati bash skript koji nudi korisniku da izlista:
#   1) izlista sve aktivne procese, 
#   2) izlista sve procese zadatog korisnika (iskoristiti USER promenljivu okruzenja),
#   3) odredi pid procesa za zadato ime komande
# 
# Promenljiva okruzenja Z5_OPT odredjuje koja od tri funkcionalnosti ce biti izvrsena.
# Ukoliko je odabrana funkcionalnost 3), promenljiva okruzenja Z5_CMDNAME treba da 
# sadrzi naziv komande za ciji se proces trazi PID (npr. ping ukoliko se trazi PID
# procesa nastalog pokretanjem komande ping). Podrzati i slucajeve kada promenljive
# okruzenja nisu definisane ili nemaju zadate vrednosti, kao i slucaj zadavanja 
# naziva komande za koju ne postoji proces.
#
# Napredni deo zadatka (opciono):
# Obezbediti da se pri izvrsavanju opcije 3 u slucaju kada je zadato ime nepostojece
# komande ne ispisuje nista drugo osim poruke da nije pronadjen PID za zadatu komandu.
#
# Argumenti:
#   - nema
#
# Primer poziva:
#   export Z5_OPT=3
#   export Z5_CMDNAME=ping
#   ./05_process_tools


# TODO implementirati  
option=$Z5_OPT
cmd=$Z5_CMDNAME

case "$option" in 
    "1")
        echo "Opcija 1"
        ps -a
        ;;
    "2")
        echo "Opcija 2"
        ps -a -U $USER
        ;;
    "3")
        echo "Opcija 3"
        # pgrep -f $cmd
        out=$(ps -a | grep "$cmd" | awk '{print $1}')
        if [[ -z $out ]]; then
            echo "Ne postoji"
        else
            for pid in $out
            do
                echo $pid
            done
            # while read pid; do
            #     echo "$pid"
            # done <<< "$out"
        fi
        ;;
    "*") echo "Nepoznata opcija"; exit 1; ;;
esac
