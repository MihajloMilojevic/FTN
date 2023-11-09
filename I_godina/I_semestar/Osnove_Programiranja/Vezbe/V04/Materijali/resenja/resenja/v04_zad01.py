if __name__ == '__main__':
    first = input("Unesite prvi string:")
    second = input("Unesite drugi string:")

    result = 2*first[:3]+second[-2::]
    print("Rezultat je", result)