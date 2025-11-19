from flask import Flask, request
import requests
import json

app = Flask(__name__)
port=8002

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

@app.route("/filter", methods=['POST'])
def filter():
    message = json.loads(request.data)
    if message["kolicina"]>9000:
        send("filtered_transactions", message)
    return "", 200

if __name__ == "__main__":
    subscribe("zadatak1", "test_grupa", "filter")
    app.run(host="localhost", port=port, debug=True)