#1.	Na osnovu stringa neparne dužine veće od 7, ispiši srednja 3 karaktera:
#Primer: ulaz: “NekiPrimeri“, izlaz: “Pri“

if __name__ == '__main__':

    user_input = input("Unesite neki string: ")

    middle_index = (len(user_input)-1)//2
    begin_range_index = middle_index - 1
    end_range_index = middle_index + 2

    print(middle_index)

    print(user_input[begin_range_index:end_range_index])

