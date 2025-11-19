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
    empty_record = {"id": -1, "name": "", "q": 0.0, "status": 0}
    # Odabrati implementaciju odgovarajuce organizacije datoteka

    binary_file = HashFile(fn, rec, F, B, empty_record)

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

    binary_file.delete_by_id_physical(35)
    binary_file.delete_by_id_physical(8)
    binary_file.delete_by_id_physical(28)

    binary_file.print_file()


if __name__ == "__main__":
    main()
