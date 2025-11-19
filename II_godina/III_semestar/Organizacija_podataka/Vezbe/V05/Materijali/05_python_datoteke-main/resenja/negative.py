#!/usr/bin/python3

SIZE_OFFSET = 2
HEADER_OFFSET = 10
WIDTH_OFFSET = 18
HEIGHT_OFFSET = 22

def get_short_at(image_file, offset):
    image_file.seek(offset)
    offset = image_file.read(2)
    return int.from_bytes(offset, 'little')

def get_int_at(image_file, offset):
    image_file.seek(offset)
    offset = image_file.read(4)
    return int.from_bytes(offset, 'little')

def get_header(image_file):
    offset = get_int_at(image_file, HEADER_OFFSET)
    image_file.seek(0)
    return image_file.read(offset)

def transform(path, out_path):
    image_file = open(path, "rb")
    out_file = open(out_path, "wb")
    
    size = get_int_at(image_file, SIZE_OFFSET)
    print(f"Size: {size} bytes")

    width = get_int_at(image_file, WIDTH_OFFSET)
    print(f"Width: {width} pixels")
    height = get_int_at(image_file, HEIGHT_OFFSET)
    print(f"Height: {height} pixels")

    header_size = get_int_at(image_file, HEADER_OFFSET)

    out_file.write(get_header(image_file))
    image_file.seek(header_size)
    
    rx = width*3//4
    ry = height*3//4

    for i in range(size-header_size):
        px = image_file.read(1)
        # inv = int.from_bytes(px, 'little') ^ 0b1111
        #inv = 255 - int.from_bytes(px, 'little')
        inv = int.from_bytes(px, 'little')
        if inv > 255:
            inv = 255
        if inv < 0:
            inv = 0

        y = (i//3)//width
        x = (i//3)%width

        if (((x-rx)**2 + (y-ry)**2) < 100**2):
            if i%3 == 0:
                inv = 0
            else:
                inv = 255

        xdiff = abs(x-rx)
        ydiff = abs(y-ry)

        if ((xdiff < 3 and ydiff < 200) or (xdiff < 200 and ydiff < 3)):
            if i%3 == 0:
                inv = 0
            else:
                inv = 255

        if (xdiff < 100*1.41 and ydiff < 100*1.41 and abs(xdiff-ydiff) < 3):
            if i%3 == 0:
                inv = 0
            else:
                inv = 255

        # if (400 <= x and x <= 800 and 200 <= y and y <= 400):
        #     if i%3 == 1:
        #         inv = 255
        #     else:
        #         inv = 0
        inv = 255 - int.from_bytes(px, 'little')
        out_file.write(inv.to_bytes(1, 'little'))
        #out_file.write(px)

    image_file.close()
    out_file.close()
    
transform("MARBLES.bmp", "out.bmp")