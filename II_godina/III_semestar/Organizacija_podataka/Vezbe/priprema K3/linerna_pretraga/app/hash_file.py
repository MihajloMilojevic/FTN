from app.binary_file import BinaryFile  # Assuming BinaryFile is defined in binary_file.py
from app.record import Record
from typing import Dict
from app.constants import RecordStatus

class HashFile(BinaryFile):
    def __init__(self,
        filename: str,
        record: Record,
        blocking_factor: int,
        number_of_buckets: int,
        empty_record: Dict,
        step: int = 1,):

        super().__init__(filename, record, blocking_factor, empty_record, empty_record["id"])
        self.bucket_size = blocking_factor * self.record_size
        self.B = number_of_buckets
        self.step = step

    def hash(self, key: int) -> int:
        return key % self.B

    def init(self):
        with open(self.filename, "wb") as file:
            for _ in range(self.B):
                bucket = [self.empty_record] * self.blocking_factor
                self.write_block(file, bucket)
    
    def insert(self, record: Dict):
        primary_bucket = self.hash(record["id"])
        current_bucket = primary_bucket
        with open(self.filename, "rb+") as file:
            for _ in range(self.B):
                file.seek(current_bucket * self.bucket_size)
                bucket = self.read_block(file)
                for i in range(self.blocking_factor):
                    if bucket[i]["id"] == self.empty_key and bucket[i]["status"] == RecordStatus.FREE:
                        #pronašli smo prazno mesto
                        bucket[i] = record
                        file.seek(current_bucket * self.bucket_size)
                        self.write_block(file, bucket)
                        return current_bucket, i
                    if bucket[i]["id"] == record["id"]:
                        print(f"Duplicate key {record['id']}")
                        return None
                # nismo našli u trenutnom bucketu, idemo na sledeći
                current_bucket = (current_bucket + self.step) % self.B
            return None
    
    def locate(self, id: int):
        primary_bucket = self.hash(id)
        current_bucket = primary_bucket
        with open(self.filename, "rb+") as file:
            for count in range(self.B):
                file.seek(current_bucket * self.bucket_size)
                bucket = self.read_block(file)
                for i in range(self.blocking_factor):
                    if bucket[i]["id"] == id:
                        if bucket[i]["status"] == RecordStatus.ACTIVE:
                            return current_bucket, i
                        return None # Obrisan
                # nismo našli u trenutnom bucketu, idemo na sledeći
                current_bucket = (current_bucket + self.step) % self.B
            return None # Nismo pronašli, a ceo krug napravili
        
    def find(self, id: int):
        cords = self.locate(id)
        if not cords:
            return None
        with open(self.filename, "rb") as file:
            file.seek(cords[0] * self.block_size)
            bucket = self.read_block(file)
            return bucket[cords[1]]

    def modify(self, updateRecord: Dict):
        cords = self.locate(updateRecord["id"])
        if not cords:
            return False
        with open(self.filename, "rb+") as file:
            file.seek(cords[0] * self.block_size)
            bucket = self.read_block(file)
            bucket[cords[1]].update(updateRecord)
            file.seek(cords[0] * self.block_size)
            self.write_block(file, bucket)
            return True
        
    def delete(self, id: int):
        return self.modify({"id": id, "status": RecordStatus.DELETED})
    
    def print(self, detailed = False):
        with open(self.filename, "rb") as file:
            for i in range(self.B):
                bucket = self.read_block(file)
                ids = [str(rec["id"]) + " (A)" if rec["status"] == RecordStatus.ACTIVE 
                                             else str(rec["id"]) + " (D)" if rec["status"] == RecordStatus.DELETED 
                                             else "*" for rec in bucket]
                print(f'Bucket {i}: {" ".join(ids)}')
                if detailed:
                    for rec in bucket:
                        print(rec)