#!/bin/bash
# testiranje rešenja zadatka sa unapred definisanim ulazima

#   Copyright 2017 Žarko Živanov
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

# exit 0 - stiglo se do testova
# exit 1 - greška u kompajliranju
# exit 2 - nije nađen fajl

TESTS=(01 02 03 04 05 06 07)
EXITS=(0 0 0 1 2 3 1)
EMPTY="#"
QUIET=0
KEEP=0
SIG=""

TEST01=$(cat <<EOL
0 00 01 1 2 014 14
EOL
)

OUTP01=$(cat <<EOL
Unesite string: 0 00 01 1 2 014 14
Suma elemenata niza je: 30
Broj oktalnih elemenata u nizu: 3
Broj decimalnih elemenata u nizu: 4
EOL
)

TEST02=$(cat <<EOL
00 01 02 03 04 05 06 07
EOL
)

OUTP02=$(cat <<EOL
Unesite string: 00 01 02 03 04 05 06 07
Suma elemenata niza je: 28
Broj oktalnih elemenata u nizu: 8
Broj decimalnih elemenata u nizu: 0
EOL
)

TEST03=$(cat <<EOL
0 1 2 3 4 5 6 7 8 9
EOL
)

OUTP03=$(cat <<EOL
Unesite string: 0 1 2 3 4 5 6 7 8 9
Suma elemenata niza je: 45
Broj oktalnih elemenata u nizu: 0
Broj decimalnih elemenata u nizu: 10
EOL
)

TEST04=$(cat <<EOL
0 01 1 , 2 02 14 f
EOL
)

OUTP04=$(cat <<EOL
Unesite string: 0 01 1 , 2 02 14 f
Doslo je do greske u izvrsavanju programa!
EOL
)

TEST05=$(cat <<EOL
 0 1 1234567899999
EOL
)

OUTP05=$(cat <<EOL
Unesite string:  0 1 1234567899999
Doslo je do greske u izvrsavanju programa!
EOL
)

TEST06=$(cat <<EOL
5 0789 4294967294
EOL
)

OUTP06=$(cat <<EOL
Unesite string: 5 0789 4294967294
Doslo je do greske u izvrsavanju programa!
EOL
)

TEST07=$(cat <<EOL
5 f 0789 4294967294
EOL
)

OUTP07=$(cat <<EOL
Unesite string: 5 f 0789 4294967294
Doslo je do greske u izvrsavanju programa!
EOL
)

function echoq {
    if [ $QUIET -eq 0 ]; then
        echo "$@"
    fi
}

if [ "$1" == "-q" ]; then
    QUIET=1
    shift
fi
if [ "$1" \> "00" ] && [ "$1" \< "99" ]; then
    TESTS=($1)
    KEEP=1
    shift
fi

if [ "$1" != "" ] && [ -f "$1" ]; then
    echoq -e "\n\e[01;32mKompajliranje...\e[00m"
    grep ".text" $1 1>/dev/null 2>/dev/null && (grep ".globl" $1 1>/dev/null 2>/dev/null || grep ".global" $1 1>/dev/null 2>/dev/null)
    if [ $? -ne 0 ]; then
        echoq -e "\e[01;31m\n\nNije asemblerski program!\e[00m\n"
        exit 1
    fi
    GLAVNI=""
    if [ $(grep -c "main:" $1) == "0" ]; then
        if [ -f glavni.c ]; then
            GLAVNI=glavni.c
        else
            echoq -e "\e[01;31m\n\nNije nađen glavni.c!\e[00m\n"
        fi
    fi
    #nalaženje fajlova od kojih se sastoji rešenje
    zfiles=$(grep -E "^[[:space:]]*#[[:space:]]*fajlovi[[:space:]]*:" $1)
    if [ "$zfiles" != "" ]; then
        zfiles=${zfiles#*:}
    else
        zfiles="$@"
    fi
    gcc -g -m32 -o zad $GLAVNI $zfiles 1>out1 2>&1
    if [ $? -ne 0 ]; then
        echoq -e "\e[01;31m\n\nGreška u kompajliranju!\e[00m\n"
        if [ $QUIET -eq 0 ]; then
            cat out1
        else
            echo "0"
        fi
        rm -f out1
        exit 1
    fi
else
    if [ "$1" != "" ]; then
        echoq -e "\e[01;31mFajl \"$1\" nije nađen!\e[00m"
    fi
    lasttest=${TESTS[${#TESTS[@]}-1]}
    echoq -e "\n\e[01;32mUpotreba:\e[00m"
    echoq -e "\e[01;34m$0 [-q] [TT] \e[01;32mime_programa.S\e[00m"
    echoq -e "Opcija -q ispisuje samo procenat uspešnih testova"
    echoq -e "Opcija TT (01<=TT<=$lasttest) pokreće samo zadati test i ispisuje diff izlaz za njega\n"
    if [ $QUIET -ne 0 ]; then
        echo "0"
    fi
    exit 2
fi

cat >./run <<EOL
spawn -noecho [lindex \$argv 0]
for {set i 1} {\$i < [llength \$argv]} {incr i 1} {
    sleep 0.05
    send -- "[lindex \$argv \$i]"
    send "\r"
}
expect eof
catch wait reason
set sig [lindex \$reason 5]
if {\$sig == ""} {
    set code [lindex \$reason 3]
} elseif {\$sig == "SIGFPE"} {
    set code [expr 128+8]
} elseif {\$sig == "SIGSEGV"} {
    set code [expr 128+11]
} elseif {\$sig == "SIGINT"} {
    set code [expr 128+2]
} elseif {\$sig == "SIGILL"} {
    set code [expr 128+4]
} elseif {\$sig == "SIGKILL"} {
    set code [expr 128+9]
} else {
    set code [expr 128+1]
}
exit \$code
EOL

passed=0
total=0
nn=0
for n in "${TESTS[@]}"; do
    echoq -e "\n\n\e[01;34m-----------------------------------"
    echoq "TEST $n"
    echoq -e "-----------------------------------\e[00m"
    tcode=${EXITS[$nn]}
    cor="OUTP$n"
    eval cor="\$$cor"
    echo -e "$cor" > out2
    echoq -e "\e[01;32mTAČAN IZLAZ:\e[00m"
    if [ $QUIET -eq 0 ]; then
        cat out2
    fi
    echoq -e "Izlazni kod: \e[01;32m$tcode\e[00m"
    tst="TEST$n"
    eval tst=\$$tst
    oldIFS="$IFS"; IFS=$'\n'
    tst=($tst)
    IFS="$oldIFS"
    lin=${#tst[*]}
    for ((l=0; l<lin; l++ )); do
        if [ "${tst[$l]}" == "$EMPTY" ]; then
            eval tst[$l]=""
        fi
    done
    ok=1
    expect run ./zad "${tst[@]}" 1>out1 2>&1
    code=$?
    sed -i -e '$a\' out1
    sed -i 's/\x0//g' out1
    sed -i 's/\xd//g' out1
    sed -i '/^$/d' out1
    sed -i 's/\x0//g' out1
    for ((i=1; i<32; i++)); do
        if [ $i -ne 9 ] && [ $i -ne 10 ] && [ $i -ne 13 ]; then
            hex=$(printf '%X' $i)
            sed -i "s/\x$hex/[0x$hex]/g" out1
        fi
    done
    for ((i=128; i<256; i++)); do
        hex=$(printf '%X' $i)
        sed -i "s/\x$hex/[0x$hex]/g" out1
    done
    echoq -e "\e[01;34m\nVAŠ IZLAZ:\e[00m"
    if [ $QUIET -eq 0 ]; then
        cat out1
    fi
    diff -q -a -w out1 out2 1>/dev/null 2>/dev/null
    if [ $? -eq 0 ]; then
        echoq -e "\e[01;32m\nIzlazi se poklapaju.\e[00m"
    else
        echoq -e "\e[01;31m\nIzlazi se NE poklapaju!\e[00m"
        ok=0
    fi
    if [ $code -gt 127 ]; then
        code=$((code-128))
        sig=""
        if [ $code -eq 8 ]; then sig=" (SIGFPE - Floating point exception)"; fi
        if [ $code -eq 11 ]; then sig=" (SIGSEGV - Invalid memory segment access)"; fi
        echoq -e "\n\e[01;31mProgram je vratio Fatal error signal $code$sig!\e[00m"
        ok=0
        SIG="(zbog \e[01;31mexception\e[00m-a) "
    elif [ $code -eq $tcode ]; then
        echoq -e "\nIzlazni kod: \e[01;32m$code\e[00m"
    else
        echoq -e "\n\e[01;31mPogrešan izlazni kod: $code\e[00m"
        ok=0
    fi
    total=$((total + 1))
    if [ $ok -eq 1 ]; then
        passed=$((passed + 1))
    fi
    nn=$((nn+1))
done
percent=$((passed * 100 / total))
if [ "$SIG" != "" ]; then
    percent=0
fi
echoq -e "\n\n\e[01;34m-----------------------------------"
echoq "Ukupan rezultat"
echoq -e "-----------------------------------\e[00m"
if [ $passed -eq $total ]; then
    col="\e[01;32m"
else
    col="\e[01;31m"
fi
echoq -e "Prošlo je ${col}${passed}\e[00m od \e[01;32m${total}\e[00m automatskih testova, odnosno ${SIG}${col}${percent}%.\e[00m\n"
if [ $KEEP -eq 0 ]; then
    rm -f zad run out1 out2 1>/dev/null 2>/dev/null
else
    rm -f run 1>/dev/null 2>/dev/null
    #diff -u -a -w out1 out2
fi
if [ $QUIET -ne 0 ]; then
    echo $percent
fi
if [ "$SIG" != "" ]; then
    exit 3
else
    exit 0
fi


