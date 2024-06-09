from os import listdir
from os.path import isfile, join, isdir

def print_files(search_path, depth = 0):
    for f in all_files(search_path):
        print("\t" * depth + f)
    for dir in all_dirs(search_path):
        print("\t"*depth + dir + ":")
        print_files(join(search_path, dir), depth+1)
    

def all_files(search_path):
    return [f for f in listdir(search_path) if isfile(join(search_path, f))]

def all_dirs(search_path):
    return [f for f in listdir(search_path) if isdir(join(search_path, f))]

def main():
    search_path = input("Unesite putanju: ")
    print_files(search_path)

if __name__ == "__main__":
    main()