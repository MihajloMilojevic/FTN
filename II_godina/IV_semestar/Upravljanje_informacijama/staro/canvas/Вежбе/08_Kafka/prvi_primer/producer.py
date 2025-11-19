import requests
import json

# Poruka treba da bude dictionary 
def send(queue_name, message):
    req = {
        "ime_niza": queue_name,
        "poruka": message
    }
    requests.post("http://localhost:9000/send", data=json.dumps(req))

if __name__ == "__main__":
    send("niz1", {"test":"poruka"})