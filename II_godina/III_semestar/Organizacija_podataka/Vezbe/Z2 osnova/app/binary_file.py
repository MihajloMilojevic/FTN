#!/usr/bin/python

import struct
from app.record import Record
from typing import BinaryIO, List, Dict


class BinaryFile:
    def __init__(
        self,
        filename: str,
        record: Record,
        blocking_factor: int,
        empty_record: Dict,
        empty_key: int = -1,
    ):
        self.filename = filename
        self.record = record
        self.record_size = struct.calcsize(self.record.format)
        self.blocking_factor = blocking_factor
        self.block_size = self.blocking_factor * self.record_size
        self.empty_record = empty_record
        self.empty_key = empty_key

    def write_block(self, file: BinaryIO, block: List[Dict]):
        binary_data = bytearray()

        for rec in block:
            rec_binary_data = self.record.dict_to_encoded_values(rec)
            binary_data.extend(rec_binary_data)

        file.write(binary_data)

    def read_block(self, file: BinaryIO):
        binary_data = file.read(self.block_size)
        block = []

        if len(binary_data) == 0:
            return block

        for i in range(self.blocking_factor):
            begin = self.record_size * i
            end = self.record_size * (i + 1)
            block.append(self.record.encoded_tuple_to_dict(binary_data[begin:end]))

        return block
