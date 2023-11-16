
def grade(points):
    if points < 0 or points > 100:
        return -1
    if points <= 54:
        return 5
    if points <= 64:
        return 6
    if points <= 74:
        return 7
    if points <= 84:
        return 8
    if points <= 94:
        return 9
    return 10
    
def main():
    print(f"Ocena je {grade(float(input('Unesi broj poena: ')))}")

if __name__ == "__main__":
    main()