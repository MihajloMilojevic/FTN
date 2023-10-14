#!/bin/bash
#dodaje funckiju za kompajliranje i otvaranje u debugeru

function m2comp() {
    echo "Compiling $1.S into $1.out"
    gcc -m32 -g -o $1 "$1.S"
    echo "Compile Done"
}

function m2deb() {
    m2comp $1
    echo "Opening $1.out in Debuger";
    ddd $1 &
}