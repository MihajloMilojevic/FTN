#!/usr/bin/python

import struct
import os
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

    def __iter__(self):
        with open(self.filename, "rb") as file:
            block_index = 0
            while True:
                block = self.read_block(file)
                if not block:
                    return
                for i in range(self.blocking_factor):
                    if block[i]["id"] == self.empty_key:
                        break
                    yield block[i], block_index, i
                block_index += 1


    def init_file(self):
        with open(self.filename, "wb") as file:
            self.write_block(file, [self.empty_record] * self.blocking_factor)

    # criteria is a function that takes a record, block index and record index
    # and returns (bool, bool) where first bool represent if that is the element
    # and second bool represents if should continue the search
    def find(self, criteria):
        items = []
        for item in self:
            is_it, should_continue = criteria(*item)
            if is_it:
                items.append(item)
            if not should_continue:
                break
        return items
    
    def print_file(self):
        for item in self:
            print(item)

    def update(self, criteria, get_new_values):
        items = self.find(criteria)
        
        with open(self.filename, "rb+") as file: 
            for _, block_index, rec_index in items:
                file.seek(block_index * self.block_size)
                block = self.read_block(file)
                new_value = get_new_values(block[rec_index])
                if "id" in new_value:
                    del new_value["id"]
                block[rec_index].update(new_value)
                file.seek(-self.block_size, 1)
                self.write_block(file, block)

        return len(items)
    
    def delete_logical(self, criteria):
        return self.update(criteria, lambda rec: {"status": 2})
    
    def __delete_physical(self, block_index, rec_index):
        with open(self.filename, "rb+") as file:
            while True:
                file.seek(block_index * self.block_size)
                block = self.read_block(file)
                for i in range(rec_index, self.blocking_factor-1):
                    block[i] = block[i+1]
                if block[-1]["id"] == self.empty_key:
                    file.seek(-self.block_size, 1)
                    self.write_block(file, block)
                    break
                next_block = self.read_block(file)
                file.seek(-2*self.block_size, 1)
                block[-1] = next_block[0]
                self.write_block(file, block)
                block_index += 1
                rec_index = 0
        os.ftruncate(os.open(self.filename, os.O_RDWR), self.block_size * (block_index + 1))
    

    def delete_physical(self, criteria):
        count = 0
        items = self.find(criteria)
        for _, block_index, rec_index in items:
            rec_index -=  count
            while rec_index < 0:
                rec_index += self.blocking_factor
                block_index -= 1
            self.__delete_physical(block_index, rec_index)
            count += 1
        return count


        
