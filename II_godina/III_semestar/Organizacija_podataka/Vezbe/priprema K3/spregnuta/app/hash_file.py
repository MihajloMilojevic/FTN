from app.binary_file import BinaryFile
from app.record import Record
from typing import Dict, BinaryIO, Tuple, List
from app.constants import RecordStatus

class HashFile(BinaryFile):
    def __init__(self,
        filename: str,
        record: Record,
        blocking_factor: int,
        number_of_buckets: int,
        empty_record: Dict):

        super().__init__(filename, record, blocking_factor, empty_record, empty_record["id"])
        self.B = number_of_buckets

    def hash(self, key: int) -> int:
        return key % self.B

    def init(self):
        with open(self.filename, "wb") as file:
            for i in range(self.B):
                header = {"firstBlock": -1, "firstIndex": -1, "previousFree": i-1, "nextFree": i+1, "count": self.blocking_factor}
                if i == 0:
                    header["previousFree"] = -1
                if i == self.blocking_factor - 1:
                    header["nextFree"] = -1
                bucket = [self.empty_record] * self.blocking_factor
                self.write_block(file, header, bucket)
            self.write_L(file, 0)

    def _find_last_synonym(self, file:BinaryIO,  first_block: int, first_index: int):
        # Pratimo listu
        current_bucket = first_block
        current_index = first_index
        file.seek(first_block * self.block_size)
        load_new = False
        block = self.read_block(file)
        if not block:
            return None
        header, bucket = block
        for _ in range(self.B * self.blocking_factor):
            if load_new:
                block = self.read_block(file)
                if not block:
                    return None
                header, bucket = block
                load_new = False
            # Došli smo do kraja
            if bucket[current_index]["nextBucket"] == -1:
                return current_bucket, current_index
            # Idemo na sledeći blok koji se razlikuje od trenutno učitanog
            if bucket[current_index]["nextBucket"] != current_bucket:
                # Učitavamo novi bucket
                current_bucket = bucket[current_index]["nextBucket"]
                load_new = True

            # Nastavljamo na sledeći record u istom bucketu
            current_index = bucket[current_index]["nextIndex"]
        return None

    def _unlink_bucket(self, file:BinaryIO, bucket_index: int):
        file.seek(bucket_index * self.block_size)
        block = self.read_block(file)
        if not block:
            return
        header = block[0]
        bucket = block[1]
        if header["nextFree"] != -1:
            # Postoji sledeći
            file.seek(header["nextFree"] * self.block_size)
            block = self.read_block(file)
            if not block:
                return
            block[0]["previousFree"] = header["previousFree"]
            file.seek(-self.block_size, 1)
            self.write_block(file, *block)
        
        if header["previousFree"] != -1:
            # Postoji prethodni
            file.seek(header["previousFree"] * self.block_size)
            block = self.read_block(file)
            if not block:
                return
            block[0]["nextFree"] = header["nextFree"]
            file.seek(-self.block_size, 1)
            self.write_block(file, *block)
        else:
            # Nema prethodnog, znači on je bio head, moramo da promenimo L
            file.seek(-self.L_size, 2)
            self.write_L(file, header["nextFree"])
        
        header["nextFree"] = -1
        header["previousFree"] = -1
        file.seek(bucket_index * self.block_size)
        self.write_block(file, header, bucket)

    def _insert_in_empty_bucket(self, file: BinaryIO, record: Dict) -> None | Tuple[int, int]:
        file.seek(-self.L_size, 2)
        L = self.read_L(file)
        if L == -1:
            return None
        file.seek(L * self.L_size)
        block = self.read_block(file)
        if not block:
            return None
        header, bucket = block
        inserted_index = -1
        for i in range(self.blocking_factor):
            if bucket[i]["status"] == RecordStatus.FREE:
                bucket[i].update(record)
                inserted_index = i
                break
        if inserted_index == -1:
            return None
        header["count"] -= 1
        file.seek(L * self.L_size)
        self.write_block(file, header, bucket)

        if header["count"] == 0:
            self._unlink_bucket(file, L)

        return L, inserted_index

    def insert(self, record: Dict):

        found = self.locate(record["id"])
        if found:
            print("Već postoji:", record["id"])
            return None

        # Ne postoji, dodajemo novi
        primary_bucket = self.hash(record["id"])
        with open(self.filename, "rb+") as file:
            file.seek(primary_bucket * self.block_size)
            block = self.read_block(file)
            if not block:
                return None
            header, bucket = block
            inserted_bucket, inserted_index = -1, -1
            if header["count"] == 0:
                # Nema mesta u matičnom bloku
                cords = self._insert_in_empty_bucket(file, record)
                if not cords:
                    return None
                inserted_bucket, inserted_index = cords
            else:
                # Upisujemo u matični blok
                for i in range(self.blocking_factor):
                    if bucket[i]["status"] == RecordStatus.FREE:
                        bucket[i].update(record)
                        inserted_bucket = primary_bucket
                        inserted_index = i
                        break
                if inserted_index == -1:
                    return None
                if header["firstBucket"] == -1:
                    header["firstBucket"] = inserted_bucket
                    header["firstIndex"] = inserted_index
                header["count"] -= 1
                file.seek(primary_bucket * self.block_size)
                self.write_block(file, header, bucket)
                
                if header["count"] == 0:
                    self._unlink_bucket(file, primary_bucket)
        
            # Uvežemo u listu
            last = self._find_last_synonym(file, header["firstBucket"], header["firstIndex"])
            if not last:
                return None
            if last[0] == inserted_bucket and last[1] == inserted_index:
                return inserted_bucket, inserted_index
            file.seek(last[0] * self.block_size)
            block = self.read_block(file)
            if not block:
                return None
            block[1][last[1]].update({"nextBucket": inserted_bucket, "nextIndex": inserted_index})
            file.seek(-self.block_size, 1)
            self.write_block(file, *block)
            return inserted_bucket, inserted_index

    def locate(self, id: int) -> Tuple[int, int] | None:
        primary_bucket = self.hash(id)
        with open(self.filename, "rb+") as file:
            file.seek(primary_bucket * self.block_size)
            block = self.read_block(file)
            if not block:
                return None
            header, bucket = block
            # Ne postoji lista sinonima
            if header["firstBucket"] == -1:
                return None
            # Pratimo listu
            current_bucket = header["firstBucket"]
            current_index = header["firstIndex"]
            for _ in range(self.B * self.blocking_factor):
                # Pronašli smo element
                if bucket[current_index]["id"] == id:
                    return current_bucket, current_index
                # Došli smo do kraja
                if bucket[current_index]["nextBucket"] == -1:
                    return None
                # Idemo na sledeći blok koji se razlikuje od trenutno učitanog
                if bucket[current_index]["nextBucket"] != current_bucket:
                    # Učitavamo novi bucket
                    file.seek(bucket[current_index]["nextBucket"] * self.block_size)
                    # moramo da izmenimo current_index nakon što iskoristimo za pozicioniranje, a pre prepisivanje bucketa novim
                    current_index = bucket[current_index]["nextIndex"]
                    block = self.read_block(file)
                    if not block:
                        return None
                    header, bucket = block
                    continue
                # Nastavljamo na sledeći record u istom bucketu
                current_index = bucket[current_index]["nextIndex"]
            return None

        
    def find(self, id: int) -> Dict | None:
        found = self.locate(id)
        if not found:
            return None
        with open(self.filename, "rb") as file:
            file.seek(found[0] * self.block_size)
            block = self.read_block(file)
            if not block:
                return None
            item = block[1][found[1]]
            if item["status"] == RecordStatus.DELETED:
                return None
            del item["nextBucket"]
            del item["nextIndex"]
            return item
        

    def modify(self, updateRecord: Dict):
        found = self.locate(updateRecord["id"])
        if not found:
            return None
        with open(self.filename, "rb+") as file:
            file.seek(found[0] * self.block_size)
            block = self.read_block(file)
            if not block:
                return None
            updateRecord.pop("nextBucket", None)
            updateRecord.pop("nextIndex", None)
            block[1][found[1]].update(updateRecord)
            file.seek(-self.block_size, 1)
            self.write_block(file, *block)
        
    def delete(self, id: int):
        return self.modify({"id": id, "status": RecordStatus.DELETED})
    
    def print(self, detailed = False):
        with open(self.filename, "rb") as file:
            for i in range(self.B):
                block = self.read_block(file)
                if not block:
                    continue
                header, bucket = block
                ids = [str(rec["id"]) + " (A)" if rec["status"] == RecordStatus.ACTIVE 
                                             else str(rec["id"]) + " (D)" if rec["status"] == RecordStatus.DELETED 
                                             else "*" for rec in bucket]
                print(f'Bucket {i}:')
                print(f"\t({header['firstBucket']}, {header['firstIndex']}) ", end="")
                print(f"{header['previousFree'] if header['previousFree'] != -1 else '*'} ", end="")
                print(f"{header['nextFree'] if header['nextFree'] != -1 else '*'} ", end="")
                print(f"{header['count']} ")
                print()
                print("  ".join(ids))
                if detailed:
                    for rec in bucket:
                        print(rec)
                print("="*20)
            L = self.read_L(file)
            print(f"L = {L}")
