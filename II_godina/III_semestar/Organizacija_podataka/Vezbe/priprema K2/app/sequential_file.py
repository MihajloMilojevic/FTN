from app.binary_file import BinaryFile

class SequentialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_record, empty_key = -1):
        super().__init__(filename, record, blocking_factor, empty_record, empty_key)

    def __criteria(self, id):
        def res(rec, _, __):
            if rec["id"] == id:
                return True, False
            if rec["id"] > id:
                return False, False
            return False, True
        return res

    def find_by_id(self, id):
        
        items = self.find(self.__criteria(id))
        if not items:
            return None, None, None
        return items[0]
    
    def insert(self, new_rec):
        rec, _, _ = self.find_by_id(new_rec["id"])
        if rec:
            return False
        
        with open(self.filename, "rb+") as file:
            while True:
                last = False
                rec_index = 0
                block = self.read_block(file)
                for rec in block:
                    if rec["id"] == self.empty_key:
                        last = True
                        break
                for rec in block:
                    if rec["id"] == self.empty_key:
                        break
                    if rec["id"] > new_rec["id"]:
                        break
                    rec_index += 1
                if rec_index == self.blocking_factor:
                    continue
                temp = block[-1]
                for i in range(self.blocking_factor - 1, rec_index, -1):
                    block[i] = block[i-1]
                block[rec_index] = new_rec
                new_rec = temp
                file.seek(-self.block_size, 1)
                self.write_block(file, block)
                if last:
                    if block[-1]["id"] != self.empty_key:
                        self.write_block(file, [self.empty_record] * self.blocking_factor)
                    break
        return True


    def delete_by_id(self, id, logicaly = True):
        if logicaly:
            return self.delete_logical(self.__criteria(id))
        return self.delete_physical(self.__criteria(id))
    
    def update_by_id(self, id, get_new_values):
        return self.update(self.__criteria(id), get_new_values)
