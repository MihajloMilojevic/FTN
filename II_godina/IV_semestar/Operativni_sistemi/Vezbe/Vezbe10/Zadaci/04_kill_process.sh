#!/bin/bash
#
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


# TODO implementirati
case "$1" in
    "STOP") kill -s SIGSTOP $2 ;; 
    "TERM") kill -s SIGTERM $2 ;;
    "KILL") kill -s SIGKILL $2 ;;
    "INT") kill -s SIGINT $2 ;;
    "QUIT") kill -s SIGQUIT $2 ;;
    "CONT") kill -s SIGCONT $2 ;;
esac
