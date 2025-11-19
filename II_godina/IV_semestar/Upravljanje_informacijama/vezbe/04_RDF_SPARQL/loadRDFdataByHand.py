from rdflib import Graph, URIRef, Literal
from pyfuseki import FusekiUpdate

g = Graph()

g.add((URIRef('http://byHand/subject1'), URIRef('http://byHand/hasName'), Literal('Adam')))
fuseki = FusekiUpdate('http://134.209.250.243:3030', 'byHand');
fuseki.insert_graph(g)
