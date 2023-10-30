# Konverzija temperature iz Farenhajta u Celzijuse

if __name__ == '__main__':

    fahrenheit = eval(input("Unesite temperaturu u F >> "))
    celsius = (fahrenheit - 32)*5/9
    print("Temperatura je", celsius, "stepeni Celzijusa.")
