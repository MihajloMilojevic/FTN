#!/usr/bin/python

from app.record import Record
from typing import Dict
from app.serial_file import SerialFile
from app.sequential_file import SequentialFile
import app.constants as constants

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
    record = Record(constants.ATTRIBUTES, constants.FMT, constants.CODING)
    file = SequentialFile("data/test.bin", record, constants.F, {"id": -1, "name": "", "q": 0, "status": 0}, -1)
    file.init_file()

    rows = read_txt("data/in.txt")
    for i in range(0, len(rows)):
        file.insert(rows[i])

    print("="*20)
    for rec, _, _ in file:
        if rec["status"] == 1:
            print(rec["id"], end=" ")
    print()
    print("="*20)
    # Trazenje
    # print(file.find_by_id(49))
    # print(file.find_by_id(35))

    # file.update_by_id(4, lambda rec: ({"name": "Pera", "q": 3.14}))

    # file.delete_physical(lambda rec, bi, ri: (rec["name"].startswith("PRL"), True))
    # print("="*20)
    # for rec, _, _ in file:
    #     if rec["status"] == 1:
    #         print(rec["id"], end=" ")
    # print()
    # print("="*20)
    for i in range(5):
        file.delete_by_id(i, False)
        print("="*20)
        for rec, _, _ in file:
            if rec["status"] == 1:
                print(rec["id"], end=" ")
        print()
        print("="*20)



    # print(file.delete_by_id(8, False), 8)
    # print("="*20)
    # for rec, _, _ in file:
    #     if rec["status"] == 1:
    #         print(rec["id"], end=" ")
    # print()
    # print("="*20)


    # print(file.delete_by_id(28, False), 28)
    # print("="*20)
    # for rec, _, _ in file:
    #     if rec["status"] == 1:
    #         print(rec["id"], end=" ")
    # print()
    # print("="*20)


    

if __name__ == "__main__":
    main()
