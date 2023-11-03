if __name__ == '__main__':
    file_happy = open("../fajlovi/happy.txt", "r")
    file_primes = open("../fajlovi/primes.txt", "r")
    file_overlap = open("../fajlovi/overlap.txt", "w")

    line_happy = file_happy.readline().replace("\n", "")
    line_primes = file_primes.readline().replace("\n", "")

    while line_happy != "" and line_primes != "":
        number_happy = int(line_happy)
        number_prime = int(line_primes)

        if number_happy == number_prime:
            file_overlap.write(str(number_prime)+"\n")
            line_happy = file_happy.readline().replace("\n", "")
            line_primes = file_primes.readline().replace("\n", "")

        elif number_happy < number_prime:
            line_happy = file_happy.readline().replace("\n", "")

        else:
            line_primes = file_primes.readline().replace("\n", "")


    file_overlap.close()
    file_happy.close()
    file_primes.close()
