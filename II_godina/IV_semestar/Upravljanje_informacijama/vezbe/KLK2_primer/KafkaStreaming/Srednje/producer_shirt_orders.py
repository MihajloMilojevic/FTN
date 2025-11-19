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
    tshirt_brands = ["Nike", "Adidas", "Polo", "Uniqlo"]
    tshirt_size = ["XXL", "XL", "L", "M", "S"]
    
    for _ in range(100):
        send('srednji_zadatak', {
            'brand': random.choice(tshirt_brands),
            'size': random.choice(tshirt_size)
        })