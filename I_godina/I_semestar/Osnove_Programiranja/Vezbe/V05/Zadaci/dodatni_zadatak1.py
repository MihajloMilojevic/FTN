import math

def palindrom(string: str) -> bool:
    return string == string[::-1]

def main():
    print("Program proverava da li je string palindrom")
    string = input("Unesi string: ")

    print(f"String '{string}' {'jeste' if palindrom(string) else 'nije'} palindrom")


if __name__ == "__main__":
    main()