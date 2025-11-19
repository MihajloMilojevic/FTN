from rdflib import Graph, URIRef, Literal
from pyfuseki import FusekiUpdate

g = Graph()

g.add((URIRef('http://byHand/subject1'), URIRef('http://byHand/hasName'), Literal('Adam')))
fuseki = FusekiUpdate('http://161.35.68.117:3030', 'byHand');
fuseki.insert_graph(g)
