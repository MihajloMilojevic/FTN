
def uskrs(year: int):
    if year < 1982 or year > 2048:
        return "Godina nije u predviđenom opsegu."
    a=year%19
    b=year%4
    c=year%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7
    dan = 22+d+e
    april = dan > 31
    if dan > 31:
        dan -= 31
    return f"Uskrs je {dan} {'aprila' if april else 'marta'} {year}. godine."

def main():
    print(uskrs(int(input("Unesite godinu: "))))

if __name__ == "__main__":
    main()