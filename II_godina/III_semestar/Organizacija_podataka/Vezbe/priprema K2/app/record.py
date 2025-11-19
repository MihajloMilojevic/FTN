#!/usr/bin/python

import struct
from typing import List, Dict


class Record:
    def __init__(self, attributes: List, format: str, coding: str):
        self.attributes = attributes
        self.format = format
        self.coding = coding

    def encoded_tuple_to_dict(self, binary_data: bytes):
        t = struct.unpack(self.format, binary_data)
        return {self.attributes[i]: t[i].decode(self.coding).strip('\x00') if isinstance(t[i], bytes) else t[i] for i in range(len(t))}

    def dict_to_encoded_values(self, d: Dict):
        values = [v.encode(self.coding) if isinstance(v, str) else v for v in d.values()]
        return struct.pack(self.format, *values)
