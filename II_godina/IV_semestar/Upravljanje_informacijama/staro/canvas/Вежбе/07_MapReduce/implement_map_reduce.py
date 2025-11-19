import textwrap

# Dodatni napredni bonus zadatak: Pogledajte sadrza csv fajla SalesJan2009. Treba da se za svaku drzavu nadje najskuplja transakcija za svaku od kreditnih kartica:
# Primer resenja:
# Amerika - [visa-1200,Mastercard-3420,dina-1234,amex-3452]
# Srbija - [visa-1111, mastercard-2341,dina-1167]

# Pomocna funkcija za pretvaranje hash mape (dict) u listu parova. Trebace vam u map_implementatipon funkciji
def dict_to_list_of_tuples(dict):
    list_of_tuples = []

    #Ako imate python 3 umesto dict.iteritems() treba da stavite dict.items()
    for key, value in dict.items():
        list_of_tuples.append((key,value))

    return list_of_tuples

# Treba da vrati list key-value parova (u pythonu to moze biti lista tuple-ova)
# Data argument ce biti string 
def map_function_implementation(data):
    pass
    

def shuffle_implementation():
    pass

#Uzima listu key-value parova, treva ba vrati listu key-value parova
def reduce_function_implementation(data):
    pass

if __name__=="__main__":
    with open("./data/dq.txt") as f:
        data = f.read()

    # Podela fajla na 4 manje delove koji ce se 'paralelno' obradjivati
    data_chunks=textwrap.wrap(data,len(data)/4)

    returned_data=[]
    for chunk in data_chunks:
        ret_word_count = map_function_implementation(chunk)
        #Spajamo sve sto nam vrati svaka 'instanca' map funkcije u jednu list
        returned_data.extend(ret_word_count)
    
    final_result = reduce_function_implementation(returned_data)
    print(len(returned_data))
    print(len(final_result))

    # Sta ako hocemo da pokrenemo 2 instance reduce funkcije? Da li ce algoritam ispravno raditi?
    # Hint: nece. Sto, i kako prepraviti kod da vrati pravilan rezultat
    # Kod ispod otkomentarisati kad uradite map i reduce funkcije

    # first_half = returned_data[:len(returned_data)//2]
    # second_half = returned_data[len(returned_data)//2:]

    # final_result = reduce_function_implementation(first_half)
    # final_result.extend(reduce_function_implementation(second_half))
    # print(len(final_result))
