import requests
import random
import json

# Poruka treba da bude dictionary 
def send(queue_name, message):
    req = {
        "ime_niza": queue_name,
        "poruka": message
    }
    requests.post("http://localhost:9000/send", data=json.dumps(req))

if __name__ == "__main__":
    moguci_tipovi_kartica = ['MasterCard', 'Visa', 'Dina', 'American Express']

while True:
    n = int(input("Koliko transakcija zelite da generisete: "))
    for _ in range(n):
        send('zadatak1', {
            'tip_kartice': random.choice(moguci_tipovi_kartica),
            'kolicina': random.randint(100,10000)
        })
    send("niz1", {"test":"poruka"})