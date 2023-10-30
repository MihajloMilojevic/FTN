# convert.py
# Konverzija temperature iz Celzijusa u Farenhajte

def convert(celsius):
    return 9/5 * celsius + 32

print("Temperatura u Celzujisima i Farenhajtima:")
for c in range(0, 101, 10):
    print(f"{c}C -> {convert(c)}F")
