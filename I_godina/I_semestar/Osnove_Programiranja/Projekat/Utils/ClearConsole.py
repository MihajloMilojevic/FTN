import os


def clear():

    if os.name == "nt":         # Windows
        _ = os.system("cls")
    else:                       # Linux or Mac
        _ = os.system("clear")
