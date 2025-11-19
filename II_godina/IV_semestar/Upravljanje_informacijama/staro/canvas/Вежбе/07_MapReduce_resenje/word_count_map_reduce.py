import textwrap

# Pomocna funkcija za pretvaranje hash mape (dict) u listu parova. Trebace vam u map_implementatipon funkciji
def dict_to_list_of_tuples(dict):
    list_of_tuples = []

    #Ako imate python 3 umesto dict.iteritems() treba da stavite dict.items()
    for key, value in dict.items():
        list_of_tuples.append((key,value))

    return list_of_tuples

# Treba da vrati list key-value parova (u pythonu to moze biti lista tuple-ova)
def map_function_implementation(data):
    words = data.split()
    key_value_pairs = [(word, 1) for word in words]
    return key_value_pairs

#Uzima listu key-value parova, treva ba vrati listu key-value parova sortirano po key elementu
def shuffle(data):
    data.sort(key=lambda x : x[0])
    return data

#Uzima listu key-value parova, treva ba vrati listu key-value parova
def reduce_function_implementation(data):
    sum_dict = {}
    for pair in data:
        if pair[0] in sum_dict:
            sum_dict[pair[0]] = sum_dict[pair[0]] + pair[1]
        else:
            sum_dict[pair[0]] = pair[1]
    return dict_to_list_of_tuples(sum_dict)

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

    # Sta ako hocemo da pokrenemo 2 instance reduce funkcije? Hoce raditi algoritam ispravno?
    # Hint: nece. Sto, i kako prepraviti kod da vrati pravilan rezultat
    # Kod ispod otkomentarisati kad uradite map i reduce funkcije

    returned_data = shuffle(returned_data)
    devide_index = len(returned_data)//2
    while returned_data[devide_index-1][0] == returned_data[devide_index][0]:
        devide_index += 1
    first_half = returned_data[:devide_index]
    second_half = returned_data[devide_index:]

    final_result = reduce_function_implementation(first_half)
    final_result.extend(reduce_function_implementation(second_half))
    print(len(final_result))
