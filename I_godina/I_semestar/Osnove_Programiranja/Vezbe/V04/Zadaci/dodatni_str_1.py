def main():
    string = input("Unesi string: ")
    if len(string) % 2 == 0 or len(string) <= 7:
        print("Greška! String mora biti neparne dužine veće od 7")
        return
    mid = len(string) // 2
    print(string[mid-1: mid+2])
 
if __name__ == "__main__":
    main()