from rdflib import Graph
from pyfuseki import FusekiUpdate

g = Graph()

g.parse('./data/rdf/person_metadata.nt')
#g.parse('./data/rdf/person_metadata.rdf')
fuseki = FusekiUpdate('http://161.35.68.117:3030', 'fromFile');
fuseki.insert_graph(g)
