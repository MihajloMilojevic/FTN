import json
import requests
import pprint

query = \
"""
SELECT * WHERE { 
	?person <http://www.ftn.uns.ac.rs/rdf/examples/predicate/hobby> ?hobby .
	?person <http://www.ftn.uns.ac.rs/rdf/examples/predicate/profession> ?profession .
  	?person <http://www.ftn.uns.ac.rs/rdf/examples/predicate/livesIn> ?location .
}
"""

result = requests.post('http://134.209.250.243:3030/prlemajmun/sparql', 
    params={'query': query})
result = result.json()['results']['bindings']

print(json.dumps(result, indent=4, separators=(',', ': ')))
