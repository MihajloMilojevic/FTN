#!/bin/bash

# Napisati bash skript koji omogucava korisniku da pozove jedan od cetiri signala
# nad procesom zadatim sa pid-om. Signal koji se salje procesu i pid procesa se 
# prosledjuju kao argumenti komandne linije. Signali koje treba podrzati su
# SIGSTOP (kod 19), SIGKILL (kod 9), SIGTERM (kod 15) i SIGCONT (kod 18).
# 
# Argumenti:
#   $1 - signal
#   $2 - PID procesa kojem se salje signal
#
# Primer poziva:
#   ./04_kill_process.sh STOP <pid-procesa>


opt=$1
pid=$2

case $opt in
    STOP)
        echo 'Iniciran signal SIGSTOP.'
        kill -s SIGSTOP $pid    # moze i kill -19 $pid
        ;;
    KILL)
        echo 'Iniciran signal SIGKILL.'
        kill -s SIGKILL $pid    # moze i kill -9 $pid   
        ;;
    TERMINATE)
        echo 'Iniciran signal SIGTERM.'
        kill -s SIGTERM $pid    # moze i kill -15 $pid
        ;;
    CONTINUE)
        echo 'Iniciran signal SIGCONT.'
        kill -s SIGCONT $pid    # moze i kill -18 $pid
        ;;
    *) echo "Nepoznata opcija $opt."
esac

