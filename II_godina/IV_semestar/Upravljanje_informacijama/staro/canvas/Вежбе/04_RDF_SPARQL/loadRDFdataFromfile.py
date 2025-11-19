from rdflib import Graph
from pyfuseki import FusekiUpdate


fuseki = FusekiUpdate('http://161.35.68.117:3030', 'fromFile');
g = Graph()
g.parse('./data/rdf/person_metadata.nt')
fuseki.insert_graph(g)
