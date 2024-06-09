
def sum(n):
    if (n <= 0):
        return 0
    return n + sum(n-1)

def main():
    n = int(input("Unesi broj: "))
    print(f"Suma prvih {n} prirodnih brojeva je {sum(n)}")

if __name__ == "__main__":
    main()