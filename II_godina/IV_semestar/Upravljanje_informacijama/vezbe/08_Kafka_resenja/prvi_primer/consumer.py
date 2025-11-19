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

@app.route("/consumer1", methods=['POST'])
def consumer1():
    message = json.loads(request.data)
    print(json.dumps(message, indent=2))
    return "", 200

@app.route("/consumer2", methods=['POST'])
def consumer2():
    print("CONSUMERrrr 2")
    message = json.loads(request.data)
    print(json.dumps(message, indent=2))
    return "", 200


if __name__ == "__main__":
    subscribe("niz1", "test_grupa", "consumer1")
    subscribe("niz2", "test_grupa", "consumer2")
    app.run(host="localhost", port=port, debug=True)
