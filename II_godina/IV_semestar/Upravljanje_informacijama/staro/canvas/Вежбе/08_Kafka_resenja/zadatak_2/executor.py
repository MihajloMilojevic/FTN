from flask import Flask, request
from threading import Thread
import requests
import time
import json

app = Flask(__name__)
port=8002

executing_queries={}
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

def simulate_execution(result):
    time.sleep(1)
    del executing_queries[result['id']]
    result['result']="Query executed" 
    send("query_results", result)

@app.route("/execute", methods=['POST'])
def execute():
    message = json.loads(request.data)
    result = {'id': message['id']}
    if message['valid']==False:
        result['result']="Query not valid"
        send("query_results", result)
    elif message['id'] in executing_queries:
        result['result']="Entity locked"
        send("query_results", result)
    else:
        executing_queries[message['id']]=True
        t = Thread(target=simulate_execution, args=(result,))
        t.start()
    return "", 200

if __name__ == "__main__":
    subscribe("validated_queries", "test_grupa", "execute")
    app.run(host="localhost", port=port, debug=False)