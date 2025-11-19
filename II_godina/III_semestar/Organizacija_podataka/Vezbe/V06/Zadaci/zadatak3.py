
import struct

IN_FILE = "username.bin"
FORMAT = "12si10s10s"
ENCODING = "ascii"
RECORD_SIZE = struct.calcsize(FORMAT)
BLOCK_FACTOR = 3
BLOCK_SIZE = BLOCK_FACTOR * RECORD_SIZE

def read_block(filename, block_num):
    with open(filename, "rb") as fin:
        fin.seek((block_num - 1) * BLOCK_SIZE)
        block_bytes = fin.read(BLOCK_SIZE)
        records = []
        for i in range(BLOCK_FACTOR):
            record_bytes = block_bytes[i * RECORD_SIZE:(i + 1) * RECORD_SIZE]
            record = struct.unpack(FORMAT, record_bytes)
            record = [v.decode(ENCODING).strip('\x00') if isinstance(v, bytes) else v for v in record]
            records.append(record)
        return records

if __name__ == '__main__':
    block_num = 2
    records = read_block(IN_FILE, block_num)
    for record in records:
        print(record)