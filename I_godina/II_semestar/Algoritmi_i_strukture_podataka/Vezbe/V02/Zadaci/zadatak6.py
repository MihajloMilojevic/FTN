
def get_digit(digit):
    if digit < 10:
        return str(digit)
    return chr(ord("A")+digit-10)

def convert(n, b):
    if n < b: 
        return get_digit(n)
    return convert(n//b, b) + get_digit(n%b)

def main():
    n = int(input("Unesi broj: "))
    b = int(input("Unesi osnovu: "))
    print(convert(n, b))

if __name__ == "__main__":
    main()