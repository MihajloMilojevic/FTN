def main():
    str1 = input("Unesi string 1: ")
    if len(str1) % 2 == 0 or len(str1) <= 2:
        print("Greška! String mora biti neparne dužine veće od 2")
        return
    str2 = input("Unesi string 2: ")
    if len(str2) % 2 == 0 or len(str2) <= 2:
        print("Greška! String mora biti neparne dužine veće od 2")
        return
    rez = str1[0] + str2[0] + str1[len(str1)//2] + str2[len(str2)//2] + str1[-1] + str2[-1]
    print(rez)
 
if __name__ == "__main__":
    main()