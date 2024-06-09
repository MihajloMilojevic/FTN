
def replicate(n, k):
    if k <= 0:
        return []
    res = replicate(n,k-1)
    res.append(n)
    return res

def main():
    n = int(input("Unesi broj koji se ponavlja: "))
    k = int(input("Unesi broj ponavljanja: "))
    print(replicate(n, k))

if __name__ == "__main__":
    main()