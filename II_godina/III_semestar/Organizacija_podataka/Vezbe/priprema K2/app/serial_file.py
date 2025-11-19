from app.binary_file import BinaryFile

class SerialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_record, empty_key = -1):
        super().__init__(filename, record, blocking_factor, empty_record, empty_key)

    def find_by_id(self, id):
        items = self.find(lambda rec, bi, ri: (rec["id"] == id, rec["id"] != id))
        if not items:
            return None, None, None
        return items[0]
        
    
    def insert(self, new_rec):
        rec, _, _ = self.find_by_id(new_rec["id"])
        if rec:
            return False
        with open(self.filename, "rb+") as file:
            file.seek(-self.block_size, 2)
            block = self.read_block(file)
            for i in range(self.blocking_factor):
                if block[i]["id"] == self.empty_key:
                    break
            block[i] = new_rec
            file.seek(-self.block_size, 2)
            self.write_block(file, block)
            if i == self.blocking_factor - 1:
                self.write_block(file, [self.empty_record] * self.blocking_factor)
        return True

    def delete_by_id(self, id, logicaly = True):
        if logicaly:
            return self.delete_logical(lambda rec, bi, ri: (rec["id"] == id, rec["id"] != id))
        return self.delete_physical(lambda rec, bi, ri: (rec["id"] == id, rec["id"] != id))
    
    def update_by_id(self, id, get_new_values):
        return self.update(lambda rec, bi, ri: (rec["id"] == id, rec["id"] != id), get_new_values)
