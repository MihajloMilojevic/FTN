
def kazna(izmereno, ogranicenje):
    if izmereno <= ogranicenje:
        return "niste prekoracili brzinu"
    kazna = 5000 + (izmereno - ogranicenje) * 500 + (10000 if izmereno > 120 else 0)
    return f"vasa kazna iznosi {kazna}din"

def main():
    iz = int(input("Unesite izmerenu brzinu: "))
    og = int(input("Unesite ogranicenje: "))
    print(kazna(iz, og))

if __name__ == "__main__":
    main()