# convert.py
# Konverzija temperature iz Celzijusa u Farenhajte

print("Program konvertuje temperaturu iz celzijusa u farenhajte")
celsius = eval(input("Unesite temperaturu u C >> "))
fahrenheit = 9/5 * celsius + 32
print("Temperatura je", fahrenheit, "stepeni Farenhajta.")
