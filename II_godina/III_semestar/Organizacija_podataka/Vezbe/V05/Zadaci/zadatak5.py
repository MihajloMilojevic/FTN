IMG = "sample_640×426.bmp"

with open(IMG, "rb") as f, open(f"{IMG}_inverted.bmp", "wb") as f2:
    f.seek(2, 0)
    size = int.from_bytes(f.read(4), "little")
    print(size)
    f.seek(10, 0)
    header = int.from_bytes(f.read(4), "little")
    print(header)
    f.seek(0, 0)
    f2.write(f.read(header+1))
    count = 0
    while True:
        byte = f.read(1)
        if count < 10:
            print(byte)
        count += 1
        if not byte:
            print("End of file", byte)
            break
        f2.write((255 - int.from_bytes(byte, "little")).to_bytes(1, "little"))
    print(f"Size: {size} bytes\nHeader: {header} bytes\nCount: {count} bytes\n{size - header - count} bytes left")

with open(IMG, "rb") as f, open(f"{IMG}_half.bmp", "wb") as f2:
    f.seek(2, 0)
    size = int.from_bytes(f.read(4), "little")	
    f.seek(10, 0)
    header = int.from_bytes(f.read(4), "little")
    f.seek(0, 0)
    f2.write(f.read(header+1))
    count = 0
    while True:
        byte = f.read(1)
        if count < 10:
            print(byte)
        count += 1
        if not byte:
            print("End of file", byte)
            break
        f2.write((255 - int.from_bytes(byte, "little")//2).to_bytes(1, "little"))
    print(f"Size: {size} bytes\nHeader: {header} bytes\nCount: {count} bytes\n{size - header - count} bytes left")

with open(IMG, "rb") as f, open(f"{IMG}_third.bmp", "wb") as f2:
    f.seek(2, 0)
    size = int.from_bytes(f.read(4), "little")	
    f.seek(10, 0)
    header = int.from_bytes(f.read(4), "little")
    f.seek(0, 0)
    f2.write(f.read(header+1))
    count = 0
    while True:
        byte = f.read(1)
        if count < 10:
            print(byte)
        count += 1
        if not byte:
            print("End of file", byte)
            break
        f2.write((255 - int.from_bytes(byte, "little")//3).to_bytes(1, "little"))
    print(f"Size: {size} bytes\nHeader: {header} bytes\nCount: {count} bytes\n{size - header - count} bytes left")

with open(IMG, "rb") as f, open(f"{IMG}_double.bmp", "wb") as f2:
    f.seek(2, 0)
    size = int.from_bytes(f.read(4), "little")	
    f.seek(10, 0)
    header = int.from_bytes(f.read(4), "little")
    f.seek(0, 0)
    f2.write(f.read(header+1))
    count = 0
    while True:
        byte = f.read(1)
        if count < 10:
            print(byte)
        count += 1
        if not byte:
            print("End of file", byte)
            break
        f2.write((255 - min(255, int.from_bytes(byte, "little")*2)).to_bytes(1, "little"))
    print(f"Size: {size} bytes\nHeader: {header} bytes\nCount: {count} bytes\n{size - header - count} bytes left")