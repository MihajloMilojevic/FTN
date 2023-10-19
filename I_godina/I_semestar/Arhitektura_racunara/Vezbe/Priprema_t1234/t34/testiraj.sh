#!/bin/bash
# testiranje rešenja zadatka sa unapred definisanim ulazima

#   Copyright 2019 Žarko Živanov
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

# provera instaliranih programa
missing=0
for prg in "expect" "sed" "diff" "grep"; do
    which $prg >/dev/null
    if [ $? -ne 0 ]; then
        missing=1
    fi
done
if [ $missing -ne 0 ]; then
\e[01;31m\n\nGreška u kompajliranju!\e[00m\n
    echo -e "\e[01;31mNedostaju paketi za rad skripta.\e[01;32m Instalirajte ih sa:\e[00m"
    echo -e "\e[01;34msudo apt install expect diffutils grep sed\e[00m\n"
    exit 1
fi

TESTS=(01 02 03 04)
EXITS=(0 0 0 0)
EMPTY="#"
QUIET=0
KEEP=0
SIG=""
OUT1=/tmp/out1

TEST01=$(cat <<EOL
3
0
1
555
EOL
)

OUTP01=$(cat <<EOL
Unesite duzinu niza (maksimalno 10): 3
Unesite elemente niza u heksadecimalnom zapisu:
niz[0]=0
niz[1]=1
niz[2]=555

Uneti elementi su:
niz[0]=00000000 00000000 00000000 00000000  (0x0)
niz[1]=00000000 00000000 00000000 00000001  (0x1)
niz[2]=00000000 00000000 00000101 01010101  (0x555)

Izlaz:
niz[0]=00000000 00000000 00000000 00000000 
niz[1]=11111111 11111111 11111111 11111111 
niz[2]=00000000 00000000 00000011 00110011 

Povratna vrednost: 37
EOL
)

TEST02=$(cat <<EOL
10
0
0
0
0
0
0
0
0
0
0
EOL
)

OUTP02=$(cat <<EOL
Unesite duzinu niza (maksimalno 10): 10
Unesite elemente niza u heksadecimalnom zapisu:
niz[0]=0
niz[1]=0
niz[2]=0
niz[3]=0
niz[4]=0
niz[5]=0
niz[6]=0
niz[7]=0
niz[8]=0
niz[9]=0

Uneti elementi su:
niz[0]=00000000 00000000 00000000 00000000  (0x0)
niz[1]=00000000 00000000 00000000 00000000  (0x0)
niz[2]=00000000 00000000 00000000 00000000  (0x0)
niz[3]=00000000 00000000 00000000 00000000  (0x0)
niz[4]=00000000 00000000 00000000 00000000  (0x0)
niz[5]=00000000 00000000 00000000 00000000  (0x0)
niz[6]=00000000 00000000 00000000 00000000  (0x0)
niz[7]=00000000 00000000 00000000 00000000  (0x0)
niz[8]=00000000 00000000 00000000 00000000  (0x0)
niz[9]=00000000 00000000 00000000 00000000  (0x0)

Izlaz:
niz[0]=00000000 00000000 00000000 00000000 
niz[1]=00000000 00000000 00000000 00000000 
niz[2]=00000000 00000000 00000000 00000000 
niz[3]=00000000 00000000 00000000 00000000 
niz[4]=00000000 00000000 00000000 00000000 
niz[5]=00000000 00000000 00000000 00000000 
niz[6]=00000000 00000000 00000000 00000000 
niz[7]=00000000 00000000 00000000 00000000 
niz[8]=00000000 00000000 00000000 00000000 
niz[9]=00000000 00000000 00000000 00000000 

Povratna vrednost: 0
EOL
)

TEST03=$(cat <<EOL
1
FFFF
EOL
)

OUTP03=$(cat <<EOL
Unesite duzinu niza (maksimalno 10): 1
Unesite elemente niza u heksadecimalnom zapisu:
niz[0]=FFFF

Uneti elementi su:
niz[0]=00000000 00000000 11111111 11111111  (0xffff)

Izlaz:
niz[0]=00000000 00000000 01010101 01010101 

Povratna vrednost: 8
EOL
)

TEST04=$(cat <<EOL
8
1
12
123
1234
12345
123456
1234567
12345678
EOL
)

OUTP04=$(cat <<EOL
Unesite duzinu niza (maksimalno 10): 8
Unesite elemente niza u heksadecimalnom zapisu:
niz[0]=1
niz[1]=12
niz[2]=123
niz[3]=1234
niz[4]=12345
niz[5]=123456
niz[6]=1234567
niz[7]=12345678

Uneti elementi su:
niz[0]=00000000 00000000 00000000 00000001  (0x1)
niz[1]=00000000 00000000 00000000 00010010  (0x12)
niz[2]=00000000 00000000 00000001 00100011  (0x123)
niz[3]=00000000 00000000 00010010 00110100  (0x1234)
niz[4]=00000000 00000001 00100011 01000101  (0x12345)
niz[5]=00000000 00010010 00110100 01010110  (0x123456)
niz[6]=00000001 00100011 01000101 01100111  (0x1234567)
niz[7]=00010010 00110100 01010110 01111000  (0x12345678)

Izlaz:
niz[0]=11111111 11111111 11111111 11111111 
niz[1]=00000000 00000000 00000000 00001110 
niz[2]=00000000 00000000 00000000 11100001 
niz[3]=11111111 11111111 11110001 11101100 
niz[4]=11111111 11111111 00011110 11000011 
niz[5]=11111111 11110001 11101100 00110010 
niz[6]=00000000 11100001 00111100 11011101 
niz[7]=11110001 11101100 00110010 00101000 

Povratna vrednost: 134
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
    gcc -g -m32 -o zad $GLAVNI $zfiles 1>$OUT1 2>&1
    if [ $? -ne 0 ]; then
        echoq -e "\e[01;31m\n\nGreška u kompajliranju!\e[00m\n"
        if [ $QUIET -eq 0 ]; then
            cat $OUT1
        else
            echo "0"
        fi
        rm -f $OUT1
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
    sleep 0.5
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
    echoq -e "\nIzlazni kod: \e[01;32m$tcode\e[00m"
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
    expect run ./zad "${tst[@]}" 1>$OUT1 2>&1
    code=$?
    sed -i -e '$a\' $OUT1
    sed -i 's/\x0//g' $OUT1
    sed -i 's/\xd//g' $OUT1
    #sed -i '/^$/d' $OUT1
    sed -i 's/\x0//g' $OUT1
    for ((i=1; i<32; i++)); do
        if [ $i -ne 9 ] && [ $i -ne 10 ] && [ $i -ne 13 ]; then
            hex=$(printf '%X' $i)
            sed -i "s/\x$hex/[0x$hex]/g" $OUT1
        fi
    done
    for ((i=128; i<256; i++)); do
        hex=$(printf '%X' $i)
        sed -i "s/\x$hex/[0x$hex]/g" $OUT1
    done
    echoq -e "\e[01;34m\nVAŠ IZLAZ:\e[00m"
    if [ $QUIET -eq 0 ]; then
        cat $OUT1
    fi
    diff -q -a -w -B $OUT1 out2 1>/dev/null 2>/dev/null
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
    rm -f zad run $OUT1 out2 1>/dev/null 2>/dev/null
else
    rm -f run 1>/dev/null 2>/dev/null
    #diff -u -a -w $OUT1 out2
fi
if [ $QUIET -ne 0 ]; then
    echo $percent
fi
if [ "$SIG" != "" ]; then
    exit 3
else
    exit 0
fi


