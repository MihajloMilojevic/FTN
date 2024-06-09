def hanoi_rec(n, src, dest, help):
    if n >= 1:
        hanoi_rec(n-1, src, help, dest)
        print(f"Pomeri sa {src} na {dest}")
        hanoi_rec(n-1, help, dest, src)



def hanoi(n):
    hanoi_rec(n, "A", "B", "C")


def main():
    n = int(input("Unesi broj diskova: "))
    hanoi(n)


if __name__ == "__main__":
    main()