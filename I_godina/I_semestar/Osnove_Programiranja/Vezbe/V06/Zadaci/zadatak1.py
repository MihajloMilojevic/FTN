
def caluclate_pay(filename, hourly_pay):
    with open(filename, "r") as file:
        for line in file.readlines():
            parts = line.replace("\n", "").split("|")
            print(f"Ime: {parts[0]}")
            hours = 0
            for i in range(1, len(parts)):
                hours += float(parts[i])
            hp = hourly_pay
            if hours > 40:
                hp *= 1.5
            print(f"Zarada: {round(hours * hp, 2)}")


def main():
    caluclate_pay("radnici.txt", 1000)

if __name__ == "__main__":
    main()