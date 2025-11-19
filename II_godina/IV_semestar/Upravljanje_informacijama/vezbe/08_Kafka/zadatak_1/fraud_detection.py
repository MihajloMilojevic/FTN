from flask import Flask, request
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

@app.route("/checkup", methods=['POST'])
def checkup():
    message = json.loads(request.data)
    print("Provera transakcije:")
    print(json.dumps(message, indent=2))
    return "", 200

if __name__ == "__main__":
    subscribe("zadatak1", "test_grupa", "checkup")
    app.run(host="localhost", port=port, debug=True)