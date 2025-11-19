#!/usr/bin/env python3
"""
Indeksiranje dokumenata koristeci Whoosh (python adaptacija Lucene-a)
Kreira pretraživ indeks od dokumenata u 'data' folderu
Upotreba: python indexing.py

Pre pokretanja treba instalirati whoosh (pip install whoosh ili pip3 install whoosh)
"""

import os
import time
import shutil
from pathlib import Path
from whoosh import fields, index

class DocumentIndexer:
  def __init__(self, data_dir="data", index_dir="search_index"):
      self.data_dir = data_dir
      self.index_dir = index_dir
      self.schema = self._create_schema()
      
  def _create_schema(self):
      """Definiše semu indeksa pretrage"""
      return fields.Schema(
        doc_id=fields.ID(stored=True, unique=True),
        filename=fields.ID(stored=True),
        filepath=fields.TEXT(stored=True),
        title=fields.TEXT(stored=True),
        content=fields.TEXT(stored=True),
        # OVDE DODAŠ NEKI NOVI NPR 
        # title_from_file=fields.TEXT(stored=True)
      file_size=fields.NUMERIC(stored=True)
    )
    
  def create_fresh_index(self):
    """Kreira potpuno novi indeks, uklanjajući postojeći"""
    try:
      if os.path.exists(self.index_dir):
        shutil.rmtree(self.index_dir)
			
			# Kreiraj novi direktorijum indeksa
      os.makedirs(self.index_dir)
      print(f"Kreiran novi direktorijum indeksa: {self.index_dir}")
			
			# Kreiraj indeks
      ix = index.create_in(self.index_dir, self.schema)
      print(f"Uspešno kreiran Whoosh indeks")
      return ix
            
    except Exception as e:
      print(f"Greška pri kreiranju indeksa: {e}")
      return None
    
  def extract_title(self, content, filename):
    """Izdvaja naslov iz sadržaja dokumenta ili koristi ime fajla"""
    # Ime fajla bez ekstenzije
    return Path(filename).stem.replace('_', ' ').title()
  # Napraviš neku sličnu funkciju koja će da izvuče prvu liniju i uzmes samo substring
  # koji nema "Title: " na početku, ili kako je već kreirano
    
  def index_documents(self):
    """Indeksira sve dokumente u data direktorijumu"""
    start_time = time.time()
        
    # Proveri da li data direktorijum postoji
    data_path = Path(self.data_dir)
    if not data_path.exists():
      print(f"Greška: Data direktorijum '{self.data_dir}' nije pronađen!")
      return False
        
    # Kreiraj novi indeks
    ix = self.create_fresh_index()
        
    # Prati statistike indeksiranja
    indexed_count = 0
    error_count = 0
    total_size = 0
        
    print(f"\nPokretanje procesa indeksiranja...")
    print(f"Data direktorijum: {data_path.absolute()}")
    print("-" * 60)
        
    txt_files = list(data_path.glob("*.txt"))
    print(f"Pronađeno {len(txt_files)} tekstualnih fajlova za indeksiranje")
        
    # Indeksiraj svaki fajl pojedinačno
    for file_path in txt_files:
      try:
        with open(file_path, 'r', encoding='utf-8') as f:
          content = f.read()
                
          # Izdvoj metapodatke
          file_size = file_path.stat().st_size
          title = self.extract_title(content, file_path.name)
          doc_id = file_path.stem  # Koristi ime fajla bez ekstenzije kao ID
                
          # Ovde pozoves tu funkciju npr
          # title_from_file = extract_title_from_file(content)

          writer = ix.writer()
                
          writer.add_document(
            doc_id=doc_id,
            filename=file_path.name,
            filepath=str(file_path),
            title=title,
            content=content,
            file_size=file_size
            # I ovde dodaš taj title
            # title_from_file=tite_from_file
          )
                
          writer.commit()
                
          indexed_count += 1
          total_size += file_size
                
        print(f"Indeksiran: {file_path.name:<30} ({file_size:,} bajtova)")
                
      except Exception as e:
        error_count += 1
        print(f"Greška pri indeksiranju {file_path.name}: {e}")
        try:
          if 'writer' in locals():
            writer.cancel()
        except:
          pass
        
    # Prikaži rezime
    elapsed_time = time.time() - start_time
    print("\n" + "=" * 60)
    print("INDEKSIRANJE ZAVRŠENO")
    print("=" * 60)
    print(f"Indeksirani dokumenti:     {indexed_count}")
    print(f"Greške:                  {error_count}")
    print(f"Ukupna veličina:          {total_size:,} bajtova ({total_size/1024:.1f} KB)")
    print(f"Vreme izvršavanja:       {elapsed_time:.2f} sekundi")
    print(f"Lokacija indeksa:         {Path(self.index_dir).absolute()}")
        
    if indexed_count > 0:
      print(f"Prosek po dokumentu:      {total_size/indexed_count:.0f} bajtova")
      print(f"Brzina indeksiranja:      {indexed_count/elapsed_time:.1f} dok/sekunda")
        
    return indexed_count > 0

def main():
  print("Indekser dokumenata - Whoosh")
  print("=" * 60)
    
  # Inicijalizuj indekser
  indexer = DocumentIndexer(data_dir="data", index_dir="search_index")
    
  # Izvrši indeksiranje
  success = indexer.index_documents()
    
  if success:
    print("\nIndeksiranje uspešno završeno")
    print(f"Indeks sačuvan u: {indexer.index_dir}")
  else:
    print("\n Indeksiranje neuspešno!")
    
  return

if __name__ == "__main__":
    main()