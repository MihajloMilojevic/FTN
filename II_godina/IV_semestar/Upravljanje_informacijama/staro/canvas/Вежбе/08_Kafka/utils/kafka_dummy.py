from flask import Flask, request
import requests
import json
import random

app = Flask(__name__)
all_queues = {}

@app.route('/create', methods=['POST'])
def create_queue():
    body = json.loads(request.data)
    if "ime" not in body:
        print("U post zahtevu se ocekuje json koji sadrzi polje 'ime'")
        return "Fali polje 'ime' u zahtevu", 400
    queue_name=body['ime']
    if queue_name in all_queues:
        print("Niz {} vec postoji".format(queue_name))
        return "Niz vec postoji", 409
    all_queues[queue_name]={}
    print("Kreiran niz {}".format(queue_name))
    print(json.dumps(all_queues, indent=2))
    return "Niz kreiran", 201

@app.route('/subscribe', methods=['POST'])
def subscribe():
    body = json.loads(request.data)
    if not all(field in body for field in ['ime_niza', 'port', 'grupa', 'ime_consumera']):
        print("U telu zahteva se ne nalaze sva potrebna polj")
        return "", 400
    if body['ime_niza'] not in all_queues:
        print("Niz sa nazivom {} ne postoji.".format(body["ime_niza"]))
        return "Niz ne postoji", 400
    # proveravamo da li consumer grupa vec postoji
    queue = all_queues[body['ime_niza']]
    group_name = body['grupa']
    if group_name in queue:
        # Proveravamo da li je bas ovaj consumer vec prijavljen 
        if (body['port'], body['ime_consumera']) in queue[group_name]:
            print("Ovaj consumer je vec prijavljen na niz {} u sklopu grupe {}".format(body['ime_niza'],group_name))
        else:
            queue[group_name].append((body['port'], body['ime_consumera']))
            print("Consumer prijavljen. Trenutno stanje nizova:")
    else:
        queue[body['grupa']]=[(body['port'], body['ime_consumera'])]
        print("Consumer prijavljen. Trenutno stanje nizova:")
    print(json.dumps(all_queues, indent=2))
    return "Consumer prijavljen", 200
        
@app.route('/send', methods=['POST'])
def send_message():
    body = json.loads(request.data)
    if not all(field in body for field in ['ime_niza', 'poruka']):
        print("U telu zahteva se ne nalaze sva potrebna polj")
        return "", 400
    # Proveravamo da li niz uopste postoji
    if body['ime_niza'] not in all_queues:
        print("Niz {} ne postoji".format(body['ime_niza']))
        print(json.dumps(all_queues, indent=2))
        return "", 400
    queue = all_queues[body['ime_niza']]
    for group_name in queue:
        consumer = random.choice(queue[group_name])
        consumer_url = "http://localhost:{}/{}".format(consumer[0],consumer[1])
        print("Poslata poruka consumeru {} u okviru grupe {}".format(consumer_url, group_name))
        print("Poruka: {}".format(body['poruka']))
        requests.post(consumer_url, data=json.dumps(body['poruka']))
    return "", 200

if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)