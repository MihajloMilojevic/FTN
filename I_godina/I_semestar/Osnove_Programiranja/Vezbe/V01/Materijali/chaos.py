#chaos.py
#Program koji ilustruje haoticno ponasanje :)

if __name__ == "__main__":
    print("Ovaj program ilustuje haoticno ponasanje")
    x = eval(input("Unesite broj izmedju 0 i 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)
