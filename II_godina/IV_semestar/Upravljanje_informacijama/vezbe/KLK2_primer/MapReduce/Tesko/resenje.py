
def parse_file(file_path: str) -> list[tuple[str, str, int]]:
    result = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                whom, who, howmuch = line.split(",")
                result.append((whom, who, int(howmuch)))
            except:
                pass
    return result

def split(data: list[tuple[str, str, int]], number_of_chunks: int) -> list[list[tuple[str, str, int]]]:
    result = []
    per_chunk = len(data) // number_of_chunks
    for i in range(number_of_chunks - 1):
        result.append(data[i*per_chunk:(i+1)*per_chunk])
    result.append(data[(number_of_chunks-1)*per_chunk:])
    return result

def map_phase(data: list[tuple[str, str, int]]) -> list[tuple[tuple[str, str], int]]:
    result = []
    for el in data:
        whom, who, howmuch = el
        if whom < who:
            result.append(((whom, who), -howmuch))
        else:
            result.append(((who, whom), howmuch))
    return result

def shufle(data: list[tuple[tuple[str, str], int]], chunks: int) -> list[list[tuple[tuple[str, str], int]]]:
    result = [[] for i in range(chunks)]
    for el in data:
        result[hash(el[0]) % chunks].append(el)
    return result


def reduce_phase(data: list[tuple[tuple[str, str], int]]) -> list[tuple[tuple[str, str], int]]:
    reducer = dict()
    for el in data:
        if el[0] in reducer:
            reducer[el[0]] += el[1]
        else:
            reducer[el[0]] = el[1]
    result = []
    for key, value in reducer.items():
        if value == 0:
            continue
        if value < 0:
            result.append(((key[1], key[0]), -value))
        else:
            result.append((key, value))
    return result

if __name__ == "__main__":
    data = parse_file("data.csv")
    chunks = split(data, 3)
    mapped = []
    for chunk in chunks:
        mapped.extend(map_phase(chunk))
    reducers = shufle(mapped, 2)
    final = []
    for reducer in reducers:
        final.extend(reduce_phase(reducer))
    for item in final:
        print(f"{item[0][0]:<5} {item[0][1]:<5} {item[1]:<5}")
