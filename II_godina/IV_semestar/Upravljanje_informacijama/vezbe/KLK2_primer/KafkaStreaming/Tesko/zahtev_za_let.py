from flask import Flask, request
import time
import random
import requests
import json
from threading import Thread

app = Flask(__name__)
port=8004



# Poruka treba da bude dictionary 
def send(queue_name, message):
    req = {
        "ime_niza": queue_name,
        "poruka": message
    }
    requests.post("http://localhost:9000/send", data=json.dumps(req))


def subscribe(queue_name, queue_group, consumer_name):
    req = {
        "ime_niza": queue_name,
        "grupa": queue_group,
        "port": port,
        "ime_consumera": consumer_name
    }

    requests.post("http://localhost:9000/subscribe", data=json.dumps(req))

@app.route("/odgovor", methods=['POST'])
def odgovor():
    message = json.loads(request.data)
    print(json.dumps(message, indent=2))
    return "", 200

def sendRequests():
    time.sleep(2)
    zahtevi = [
        {
            "id_leta": "LXA25",
            "broj_piste": 2
        },
        {
            "id_leta": "MLT11",
            "broj_piste": 3
        },
        {
            "id_leta": "FTY58",
            "broj_piste": 4
        },
        {
            "id_leta": "LPO01",
            "broj_piste": 3
        }
    ]

    for zahtev in zahtevi:
        send('zahtev', zahtev)
        time.sleep(1)


if __name__ == "__main__":
    subscribe("odgovor", "test_grupa", "odgovor")
    t = Thread(target=sendRequests)
    t.start()
    app.run(host="localhost", port=port, debug=True)
