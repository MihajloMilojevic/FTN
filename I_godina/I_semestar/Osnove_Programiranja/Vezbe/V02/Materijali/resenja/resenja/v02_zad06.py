# Konverzija temperature iz Celzijusa u Farenhajte

if __name__ == '__main__':

    for celsius in range(0, 101, 10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "stepeni Celzijusa je", fahrenheit, "stepeni Farenhajta.")
