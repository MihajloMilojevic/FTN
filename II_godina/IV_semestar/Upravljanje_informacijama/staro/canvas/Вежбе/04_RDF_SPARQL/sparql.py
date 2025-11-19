import requests
import pprint

query = """SELECT ?s WHERE 
    {?s ?o "London"}"""

result = requests.post('http://147.91.177.197:80/fromFile/sparql', 
    params={'query': query})
result = result.json()['results']['bindings']

pprint.pprint(result)
