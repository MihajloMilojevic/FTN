from rdflib import Graph
from pyfuseki import FusekiUpdate


fuseki = FusekiUpdate('http://134.209.250.243:3030', 'prlemajmun')
g = Graph()
g.parse('./data/rdf/person_metadata.nt')
fuseki.insert_graph(g)
