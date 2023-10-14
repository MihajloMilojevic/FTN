#!/bin/bash
#Kopira skriptu u /home direktorijum i omogucava izvravanje

#echo $(dirname $(readlink -f -- "$0"))
#echo $(dirname $(readlink -f -- "$0"))/.commands.sh
#exit 0
#num=$(typeset -F|grep 'm2' -c)
#echo "Num on start: $num";

unset -f m2comp
unset -f m2deb

num=$(typeset -F|grep 'm2' -c)

#echo "Num after unset: $num";
if [ $num -ne 0 ];
then
    echo "Unset failed"
fi
cp $(dirname $(readlink -f -- "$0"))/.commands.sh ~/.m2_custom_commands.sh
source ~/.m2_custom_commands.sh

num=$(typeset -F|grep 'm2' -c)
#echo "Num after source: $num";
if [ $num -ne 2 ];
then
    echo "Sourcing failed. Run 'source ~/.m2_custom_commands.sh'"
else
    echo "Setup Completed"
fi

echo "Now run: 'source ~/.m2_custom_commands.sh' to register commands" 