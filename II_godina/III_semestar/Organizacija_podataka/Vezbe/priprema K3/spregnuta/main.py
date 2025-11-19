#!/usr/bin/python

import os
import struct

from app.constants import *
from app.record import Record
from app.hash_file import HashFile


def read_txt(fn):
    rows = []
    with open(fn, "r") as f:
        for line in f.readlines():
            cols = line.split()
            rows.append({
                "id": int(cols[0]),
                "name": cols[1],
                "q": float(cols[2]),
                "status": RecordStatus.ACTIVE
            })
    return rows


def main():
    rec = Record(ATTRIBUTES, FMT, CODING)  # objekat koji definise kako nam izgledaju slogovi
    empty = {
                "id": -1,
                "name": "",
                "q": 0.0,
                "status": RecordStatus.FREE
            }
    fn = "data/sample.dat"

    # Odabrati implementaciju odgovarajuce organizacije datoteka
    # binary_file = SequentialFile(fn, rec, F)
    binary_file = HashFile(fn, rec, F, B, empty)

    # Inicijalizacija datoteke odabrane organizacije
    binary_file.init()
    # binary_file.print(True)
    # return

    # Unos slogova iz tekstualne datoteke
    rows = read_txt("data/in.txt")
    for i in range(0, len(rows)):
        binary_file.insert(rows[i])

    binary_file.print(True)

    # Trazenje
    print(binary_file.find(49))
    print(binary_file.find(35))

    binary_file.delete(35)
    binary_file.delete(8)
    binary_file.delete(28)

    binary_file.print()

    print(binary_file.find(8))
    print(binary_file.find(28))
    print(binary_file.find(35))


if __name__ == "__main__":
    main()
