#chaos.py
#Program koji ilustruje haoticno ponasanje :)

if __name__ == "__main__":
    constant = 2.0
    print("Ovaj program ilustuje haoticno ponasanje")
    x = eval(input("Unesite broj izmedju 0 i 1: "))
    for i in range(10):
        x = constant * x * (1-x)
        print(x)
