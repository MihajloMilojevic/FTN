def main():
    str1 = input("Unesi prvi string: ")
    str2 = input("Unesi drugi string: ")
    res = str1[:3]*2 + str2[-3:]
    print(res)

if __name__ == "__main__":
    main()