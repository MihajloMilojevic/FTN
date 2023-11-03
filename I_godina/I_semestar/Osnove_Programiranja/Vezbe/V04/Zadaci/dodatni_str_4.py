def palindrom(string):
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True

def main():
    string = input("Unesi string: ")
    print(f"String '{string}' {'jeste' if palindrom(string) else 'nije'} palindrom")
 
if __name__ == "__main__":
    main()