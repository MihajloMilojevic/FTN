#!/usr/bin/python

import os
import struct

from app.constants import *
from app.record import Record
from app.sequential_file import SequentialFile
from app.serial_file import SerialFile
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
                "status": 1
            })
    return rows


def main():
    rec = Record(ATTRIBUTES, FMT, CODING)  # objekat koji definise kako nam izgledaju slogovi
    fn = "data/sample.dat"

    # Odabrati implementaciju odgovarajuce organizacije datoteka
    # binary_file = SerialFile(fn, rec, F)
    binary_file = SequentialFile(fn, rec, F)
    # binary_file = HashFile(fn, rec, F, B)

    # Inicijalizacija datoteke odabrane organizacije
    binary_file.init_file()

    # Unos slogova iz tekstualne datoteke
    rows = read_txt("data/in.txt")
    for i in range(0, len(rows)):
        binary_file.insert_record(rows[i])

    binary_file.print_file()

    # Trazenje
    print(binary_file.find_by_id(49))
    print(binary_file.find_by_id(35))

    # binary_file.update_by_id(4, {"id": 4, "name": "newName", "q": 31.05, "status": 1})

    binary_file.delete_by_id(35)
    binary_file.delete_by_id(8)
    binary_file.delete_by_id(28)

    binary_file.print_file()


if __name__ == "__main__":
    main()
