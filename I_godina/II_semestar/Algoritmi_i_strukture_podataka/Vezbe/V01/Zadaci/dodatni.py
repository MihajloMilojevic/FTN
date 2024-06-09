from os import listdir
from os.path import isfile, join, isdir

def print_header(name):
    print(f"\n\t{'*'*10} {name} {'*'*10}")

def print_files(file_list):
    if len(file_list) == 0:
        return print("Nema fajlova")
    for f in file_list:
        print(f)

def all_files(search_path):
    return [f for f in listdir(search_path) if isfile(join(search_path, f))]
    

def all_py_files_absolute(search_path):
    return [join(search_path, f) for f in all_files(search_path) if f.endswith(".py")]


def longest_subfolder(search_path):
    subfolders = [f for f in listdir(search_path) if isdir(join(search_path, f))]
    lenghts = [len(all_files(join(search_path, f))) for f in subfolders]
    if len(subfolders) == 0:
        return None
    max_index = 0
    for i in range(1, len(subfolders)):
        if lenghts[i] > lenghts[max_index]:
            max_index = i
    return subfolders[max_index], lenghts[max_index]


def main():
    search_path = input("Unesite putanju: ")
    print_header("SVI FAJLOVI")
    print_files(all_files(search_path))
    print_header("APSOLUTNE PUTANJE")
    print_files(all_py_files_absolute(search_path))
    print_header("NAJVECI PODDIREKTORIJUM")
    res = longest_subfolder(search_path)
    print(f"Najveci poddirektorijum je '{res[0]}' sa {res[1]} fajlova" if res is not None else "Nema poddirektorijuma")


if __name__ == "__main__":
    main()