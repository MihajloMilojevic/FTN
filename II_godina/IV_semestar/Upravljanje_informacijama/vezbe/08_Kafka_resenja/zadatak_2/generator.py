from threading import Thread
from flask import Flask, request
import time
import requests
import json

app = Flask(__name__)
port=8003

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

def send_messages():
    time.sleep(2)
    queries = [
        {
            'id': "1",
            'query_type': "UPDATE"
        },
        {
            'id': "1",
            'query_type': "SELECT"
        },
        {
            'id': "2",
            'query_type': "SELECT"
        }
    ]

    for query in queries:
        send('queries', query)

@app.route("/receive", methods=['POST'])
def receive():
    message = json.loads(request.data)
    print(json.dumps(message, indent=2))
    return "", 200

if __name__ == "__main__":
    subscribe("query_results", "test_grupa", "receive")
    t = Thread(target=send_messages)
    t.start()
    app.run(host="localhost", port=port, debug=False)
