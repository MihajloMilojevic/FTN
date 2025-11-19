import struct

def serialize_points(input_file, output_file):
    with open(input_file, "r") as fin, open(output_file, "wb") as fout:
        points = []
        for line in fin:
            if line.strip() == "":
                continue
            points.append(list(map(float, line.strip().split())))
        count = len(points)
        dim = len(points[0])
        fout.write(struct.pack("ih", count, dim))
        for point in points:
            fout.write(struct.pack("f" * dim, *point))
    
if __name__ == "__main__":
    serialize_points("tacke2D.txt", "tacke2D.bin")
    serialize_points("tacke3D.txt", "tacke3D.bin")


    