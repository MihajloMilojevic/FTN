#!/usr/bin/env python3
"""
Pretragu dokumenata uz Whoosh (Python adaptacija Lucene-a)
Pretrazuje indeksirane dokumente kreirane od strane indexing.py

Treba da bude instaliran whoosh (pip install woosh ili ptp3 install woosh)
"""

import os
from pathlib import Path
from whoosh import index, qparser
from whoosh.query import *

class DocumentSearcher:
	def __init__(self, index_dir="search_index"):
		self.index_dir = index_dir
		self.ix = None
		self.searcher = None
		
	def open_index(self):
		"""Otvara postojeći Whoosh indeks"""
		if not os.path.exists(self.index_dir):
			print(f"Greška: Direktorijum indeksa '{self.index_dir}' nije pronađen.")
			print("Prvo treba da se pokrene indexing.py da kreirate indeks.")
			return False
			
		try:
			self.ix = index.open_dir(self.index_dir)
			self.searcher = self.ix.searcher()
			print(f"Uspešno otvoren indeks iz: {self.index_dir}")
			return True
		except Exception as e:
			print(f"Greška pri otvaranju indeksa: {e}")
			return False
	
	def close_searcher(self):
		"""Zatvara pretraživač da oslobodi resurse"""
		if self.searcher:
			self.searcher.close()
	
	def display_results(self, results, query_desc=""):
		"""Ispisuje formatirane rezultate pretrage"""
		print(f"\n{query_desc}")
		print("=" * 60)
		
		if len(results) == 0:
			print("Nisu pronađeni rezultati.")
			return
			
		print(f"Pronađeno {len(results)} rezultat(a):\n")
		
		for i, hit in enumerate(results, 1):
			print(f"[{i}] {hit['title']} (Score: {hit.score:.4f})")
			print(f"    Fajl: {hit['filename']}")
			print(f"    Veličina: {hit['file_size']:,} bajtova")
			print()
	
	def search(self, query_string, description=""):
		try:
			# Koristi MultifieldParser za pretragu kroz više polja po defaultu
			parser = qparser.MultifieldParser(["content", "title", "filename"], self.ix.schema)
			query = parser.parse(query_string)
			results = self.searcher.search(query)
			
			desc = description or f"Query: '{query_string}'"
			self.display_results(results, desc)
			
		except Exception as e:
			print(f"Greška pri izvršavanju upita '{query_string}': {e}")

def main():
	print("Pretragivalac dokumenata - Whoosh primeri pretrage")
	print("=" * 60)
	
	# Inicijalizuj pretraživač
	searcher = DocumentSearcher(index_dir="search_index")
	
	if not searcher.open_index():
		return 1
	
	try:
		# Primeri pretrage koristeći raw query stringove
		print("\n🔍 Pokretanje primera pretrage...")
		
		# 1. Jednostavne pretrage termina
		searcher.search("python", "Jednostavna pretraga termina")
		searcher.search("data", "Jednostavna pretraga termina")
		
		# 2. Boolean pretrage
		searcher.search("python AND code", "Boolean AND pretraga")
		searcher.search("java OR javascript", "Boolean OR pretraga")
		
		# 3. Pretraga fraza
		searcher.search('"machine learning"', "Pretraga tačne fraze")
		
		# 4. Wildcard pretraga
		searcher.search("prog*", "Wildcard pretraga")
		
		# 5. Pretrage specifične za polja
		searcher.search("title:example", "Pretraga polja naslova")
		searcher.search("filename:*.txt", "Pretraga polja imena fajla")
		
		# 6. Fuzzy pretraga
		searcher.search("programming~", "Fuzzy pretraga")
		
		# 7. Pojačana pretraga
		searcher.search("algorithm^2 OR function", "Pojačana pretraga")
		
		# 8. NOT pretraga
		searcher.search("python NOT java", "Boolean NOT pretraga")
		
		# 9. Range pretraga (fajlovi između 100-5000 bajtova)
		searcher.search("file_size:[1300 TO 1400]", "Range pretraga")
		
	finally:
		searcher.close_searcher()
	
	return 

if __name__ == "__main__":
	main()