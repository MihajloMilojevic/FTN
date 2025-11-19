import requests
import json

def create(queue_name):
    req = {
        "ime": queue_name
    }
    requests.post("http://localhost:9000/create", data=json.dumps(req))

if __name__ == "__main__":
    create("zadatak1")
    create("filtered_transactions")