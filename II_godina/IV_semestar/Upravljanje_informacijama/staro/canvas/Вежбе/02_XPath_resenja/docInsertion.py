import existDB
import xml.etree.ElementTree as ET

def write_to_db_from_file(db, collection_name, file_path):
    file = open(file_path, 'r')
    db.create_document(collection_name, file_path.split('/')[-1], file.read())

def execute_queries(tree, xpath, exist_db, collection, document_name):
    results = tree.findall(xpath)
    for i, result in enumerate(results):
        print('Query '+str(i)+":")
        execute_xpath_db(exist_db, document_name, collection, result.text)

def execute_xpath_db(db, doc_name, collection, xpath):
    results = db.read_document(doc_name, collection, xpath)
    print(results)

if __name__ == "__main__":
    exist_db = existDB.ExistDB(url="http://161.35.68.117:8080/exist/rest",username='admin',password='')
    write_to_db_from_file(exist_db, 'booksCollection', 'data/books.xml')

    #XPath
    xpath_tree = ET.parse('data/books_xpath.xml')
    execute_queries(xpath_tree, './/expression',exist_db,'booksCollection','books.xml')