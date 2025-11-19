import existDB
import xml.etree.ElementTree as ET

def print_xml_element(element, indent):
    print('  '*indent+'<'+element.tag, end='')
    print_attributes(element)
    print('>',end='')

    if len(list(element))>0:
        print()
        for sub_elements in element:
            print_xml_element(sub_elements, indent+1)
        print('  '*indent,end='')
    else:
        print(element.text, end='')

    print('</'+element.tag+'>')

def print_attributes(element):
    for atr in element.attrib:
        print(' '+atr+'='+element.attrib[atr], end='')


def write_to_db_from_file(db: existDB.ExistDB, collection_name, file_path):
    file = open(file_path, 'r')
    db.create_document(collection_name, file_path.split('/')[-1], file.read())

def execute_xpath_etree(element, xpath):
    results = element.findall(xpath)
    for i, result in enumerate(results):
        print('RESULT '+str(i))
        print_xml_element(result, 0)


def execute_xpath_db(db, doc_name, collection, xpath):
    results = db.read_document(doc_name, collection, xpath)
    print(results)

if __name__ == "__main__":
    exist_db = existDB.ExistDB(url="http://134.209.250.243:8080/exist/rest",username='admin',password='')
    write_to_db_from_file(exist_db, 'trial1', 'data/books.xml')

    result = exist_db.read_document('books.xml', 'trial1')
    print(result)

    # ElementTree library
    # tree = ET.parse('resenja.xml')
    # print_xml_element(tree.getroot(), 0)

    # XPath example with ElementTree library
    # xpath_tree = ET.parse('resenja.xml')
    # execute_xpath_etree(xpath_tree, './/upit')

    # execute_xpath_db(exist_db, 'uplatnice.xml', 'uplatniceColl','//uplata[position()=1]')

