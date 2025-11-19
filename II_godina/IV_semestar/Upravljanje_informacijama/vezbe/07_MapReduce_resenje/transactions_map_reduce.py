from math import ceil

# Pogledajte sadrza csv fajla SalesJan2009. Treba da se za svaku drzavu nadje najskuplja transakcija za svaku od kreditnih kartica:
# Primer resenja:
# Amerika - [visa-1200,Mastercard-3420,dina-1234,amex-3452]
# Srbija - [visa-1111, mastercard-2341,dina-1167]

# Pomocna funkcija za pretvaranje hash mape (dict) u listu parova. Trebace vam u map_implementatipon funkciji
def dict_to_list_of_tuples(dict):
    list_of_tuples = []

    for key, value in dict.items():
        list_of_tuples.append((key,value))

    return list_of_tuples

# Pomocna funkcija koja list "list" deli na "n" podlista
def split_list(list, n):
    step = ceil(len(list)/n)
    return [list[i:i + step] for i in range(0, len(list), step)]

def shuffle_implementation(data):
    data.sort(key=lambda x : x[0])
    return data

# Prvi map vraca podatke u obliku kljuc: drzava_kartica, vrednost: cena
def map_1(data):
    return [(x[2]+"_"+x[1],  int(x[0])) for x in data]

#Nalazi maksimalnu transakciju za svaki par drzava-tip_kartice
def reduce_1(data):
    max_values = {}
    for pair in data:
        if  pair[0] in max_values:
            max_values[pair[0]] = max(pair[1], max_values[pair[0]])
        else:
            max_values[pair[0]]=pair[1]
    return dict_to_list_of_tuples(max_values)

# Drugi map transformise podatke iz oblika drzava_kartica:cena u oblik drzava: [(kartica:cena)]
def map_2(data):
    processed_data=[]
    for pair in data:
        [country, card] = pair[0].split('_')
        amount = pair[1]
        processed_data.append((country, [(card, amount)]))
    return processed_data

def reduce_2(data):
    aggregated_values={}
    for pair in data:
        if pair[0] in aggregated_values:
            aggregated_values[pair[0]].extend(pair[1])
        else:
            aggregated_values[pair[0]]=pair[1]
    return dict_to_list_of_tuples(aggregated_values)

def parse_single_line(line):
    segments = line.split(',')
    if not segments[2].isnumeric():
        print(line)
    return (segments[2], segments[3], segments[7])

if __name__=="__main__":
    with open("./data/SalesJan2009.csv") as file:
        lines = [line for line in file][1:]
        processed_data=list(map(parse_single_line, lines))
    # Podela fajla na 4 manje delove koji ce se 'paralelno' obradjivati
    data_chunks=split_list(processed_data, 4)

    data_after_map1=[]
    for chunk in data_chunks:
        ret_segment = map_1(chunk)
        data_after_map1.extend(ret_segment)
    
    data_after_reduce1=reduce_1(data_after_map1)

    data_chunks=split_list(data_after_reduce1, 4)
    data_after_map2=[]
    for chunk in data_chunks:
        ret_segment = map_2(chunk)
        data_after_map2.extend(ret_segment)
    final_result = reduce_2(data_after_map2)
    print(len(final_result))