#!/usr/bin/python

import struct
from app.record import Record
from typing import BinaryIO, List, Dict, Tuple


class BinaryFile:
    def __init__(
        self,
        filename: str,
        record: Record,
        blocking_factor: int,
        empty_record: Dict,
        empty_key: int = -1,
    ):
        # Add pointers to the record
        record.attributes.extend(["nextBucket", "nextIndex"])
        record.format += "ii"
        # Update empty record
        empty_record.update({"nextBucket": -1, "nextIndex": -1})

        # Create header record
        self.header_record = Record(["firstBucket", "firstIndex", "previousFree", "nextFree", "count"], "iiiii", "ascii")
        self.header_size = struct.calcsize(self.header_record.format)

        #Create L record
        self.L_record = Record(["head"], "i", "ascii")
        self.L_size = struct.calcsize(self.L_record.format)

        self.filename = filename
        self.record = record
        self.record_size = struct.calcsize(self.record.format)
        self.blocking_factor = blocking_factor
        self.block_size = self.blocking_factor * self.record_size + self.header_size
        self.empty_record = empty_record
        self.empty_key = empty_key


    def write_block(self, file: BinaryIO, header: Dict, block: List[Dict]):
        binary_data = bytearray()

        binary_data.extend(self.header_record.dict_to_encoded_values(header))

        for rec in block:
            rec_binary_data = self.record.dict_to_encoded_values(rec)
            binary_data.extend(rec_binary_data)

        file.write(binary_data)

    def read_block(self, file: BinaryIO) -> Tuple[Dict, List[Dict]] | None:
        binary_data = file.read(self.block_size)

        block = []
        header = self.get_empty_header()

        if len(binary_data) == 0:
            return header, block
        
        header = self.header_record.encoded_tuple_to_dict(binary_data[:self.header_size])
        binary_data = binary_data[self.header_size:]
        for i in range(self.blocking_factor):
            begin = self.record_size * i
            end = self.record_size * (i + 1)
            block.append(self.record.encoded_tuple_to_dict(binary_data[begin:end]))

        return header, block

    def read_L(self, file: BinaryIO) -> int:
        binary_data = file.read(self.L_size)
        if len(binary_data) == 0:
            return -1
        return self.L_record.encoded_tuple_to_dict(binary_data)["head"]
        
    def write_L(self, file: BinaryIO, L: int):
        file.write(self.L_record.dict_to_encoded_values({"head": L}))

    def get_empty_header(self):
        return {"firstBlock": -1, "firstIndex": -1, "previousFree": -1, "nextFree": -1, "count": -1}