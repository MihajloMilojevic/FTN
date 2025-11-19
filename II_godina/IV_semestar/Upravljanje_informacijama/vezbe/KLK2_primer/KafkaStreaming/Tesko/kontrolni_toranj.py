from flask import Flask, request
import time
import random
import requests
import json

app = Flask(__name__)
port=8001

def subscribe(queue_name, queue_group, consumer_name):
    req = {
        "ime_niza": queue_name,
        "grupa": queue_group,
        "port": port,
        "ime_consumera": consumer_name
    }

    requests.post("http://localhost:9000/subscribe", data=json.dumps(req))

def send(queue_name, message):
    req = {
        "ime_niza": queue_name,
        "poruka": message
    }
    requests.post("http://localhost:9000/send", data=json.dumps(req))

@app.route("/processing", methods=['POST'])
def processing():
    message = json.loads(request.data)
    print("Zahtev:")
    print(json.dumps(message, indent=2))
    time.sleep(random.choice(list(range(1, 6))))
    reply ={
        "id_leta": message["id_leta"],
        "let_odobren": random.choice([True,True,True,False])
    }
    send("odgovori_na_zahteve", reply)
    return "", 200

if __name__ == "__main__":
    subscribe("zahtevi_za_letove", "test_grupa", "processing")
    app.run(host="localhost", port=port, debug=True)