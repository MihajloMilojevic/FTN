#chaos.py
#Program koji ilustruje haoticno ponasanje :)

if __name__ == "__main__":
    print("Ovaj program ilustuje haoticno ponasanje")
    x = eval(input("Unesite prvi broj izmedju 0 i 1: "))
    y = eval(input("Unesite drugi broj izmedju 0 i 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print(str(x).ljust(25), str(y).ljust(25))
