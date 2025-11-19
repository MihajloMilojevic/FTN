import requests
import pprint

query = """SELECT ?s WHERE 
    {?s ?o "London"}"""

result = requests.post('http://161.35.68.117:3030/fromFile/sparql', 
    params={'query': query})
result = result.json()['results']['bindings']

pprint.pprint(result)
