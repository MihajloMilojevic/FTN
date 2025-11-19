import struct

def deserialize_points(file_name):
    with open(file_name, "rb") as fin:
        count, dim = struct.unpack("ih", fin.read(struct.calcsize("ih")))
        points = []
        format = "f" * dim
        size = struct.calcsize(format)
        for i in range(count):
            point = struct.unpack(format, fin.read(size))
            points.append(point)
        return points
    
def centroid(points):
    dim = len(points[0])
    result = [0] * dim
    for point in points:
        for i in range(dim):
            result[i] += point[i]
    for i in range(dim):
        result[i] /= len(points)
    return result
    
if __name__ == "__main__":
    points2D = deserialize_points("tacke2D.bin")
    print("2D points:\n")
    for point in points2D:
        print(f"({point[0]}, {point[1]})")
    centroid2D = centroid(points2D)
    print(f"\nCentroid of 2D points: ({centroid2D[0]}, {centroid2D[1]})")
    print("\n\n3D points:\n")
    points3D = deserialize_points("tacke3D.bin")
    for point in points3D:
        print(f"({point[0]}, {point[1]}, {point[2]})")
    centroid3D = centroid(points3D)
    print(f"\nCentroid of 3D points: ({centroid3D[0]}, {centroid3D[1]}, {centroid3D[2]})")