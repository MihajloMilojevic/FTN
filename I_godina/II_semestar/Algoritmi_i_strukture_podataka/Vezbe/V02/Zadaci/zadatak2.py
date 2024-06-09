def find_max_rec(niz, start):
    if start >= len(niz):
        return None
    next_max = find_max_rec(niz, start+1)
    if next_max is None:
        return niz[start]
    return max(niz[start], next_max)

def find_max(niz):
    return find_max_rec(niz, 0)


def main():
    n = int(input("Unesi broj elemenata niza: "))
    niz = []
    for i in range(n):
        niz.append(int(input(f"{i+1}-ti element = ")))
    print(f"Maximalni element niza je: {find_max(niz)}")

if __name__ == "__main__":
    main()
