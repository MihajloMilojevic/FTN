#!/bin/bash

# Osnovni deo zadatka:
# Napisati bash skript koji nudi korisniku da izlista:
#   1) izlista sve aktivne procese, 
#   2) izlista sve procese zadatog korisnika (iskoristiti USER promenljivu okruzenja),
#   3) odredi pid procesa za zadato ime komande
# 
# Promenljiva okruzenja Z5_OPT odredjuje koja od tri funkcionalnosti ce biti izvrsena.
# Ukoliko je odabrana funkcionalnost 3, promenljiva okruzenja Z5_CMDNAME treba da 
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


opt="${Z5_OPT}"
cmdname="${Z5_CMDNAME}"

case $opt in
    # samo aktivni procesi
    1)     
        ps
        ;;
    # procesi korisnika
    2)       
        ps -U $USER
        ;;
    # pid procesa za naziv komande
    3)    
        if [[ ! -z $cmdname ]]; then
            echo "Trazenje PID-a za zadatu komandu $cmdname."

            # pronalazi PID za zadatu komandu i izlaz komande preusmerava u datoteku /tmp/tempout
            # ako $cmdname postoji, u datoteku ce biti upisano "PID\n <pid1>\n <pid2> ..."
            # ako $cmdname ne postoji, u datoteku ce biti upisano samo string "PID"
            # na ovaj nacin se sprecava ispis samo stringa PID ako zadata komanda ne postoji
            ps -C $cmdname -o pid 1>/tmp/tempout

            # ako $cmdname postoji izlaz ps komande se redirektuje echo komandi (moze da se zameni i sa cat /tmp/tempout)
            # ako $cmdname ne postoji, ispisuje se samo poruka i zanemaruje se izlaz ps komande
            [[ $? -eq 0 ]] && echo "$(</tmp/tempout)" || echo 'Nije pronadjen PID za zadatu komandu.'
            [[ -f /tmp/tempout ]] && rm /tmp/tempout
        else
            echo 'Promenljiva okruzenja "Z4_PROC" nije postavljena ili nema dodeljenu vrednost.'
        fi
        ;;
    *) echo 'Promenljiva okruzenja "Z5_OPT" nije postavljena ili nema dodeljenu vrednost.'
        ;;
esac
