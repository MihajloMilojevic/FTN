/*
Napraviti thread-safe jednostruko spregnutu listu ciji cvorovi sadrze cele brojeve. 
Testirati rad liste datim glavnim programom.
*/

class LinkedList {
    public:
        LinkedList();
        void addElement(int content); //dodavanje na kraj liste novog cvora u listu sa prosledjenim sadrzajem
        void deleteElement(); //brisanje prvog cvora liste
        void insertElement(int content, int index); //ubacivanje novog cvora u listu na poziciju specificiranu parametrom "index"
        ~LinkedList();
        friend ostream& operator<<(ostream& os, LinkedList& list); //ispis elemenata liste u stream
};

void add(LinkedList& l) {
    for (int i = 0; i < 10; i++) {
        l.addElement(i);
    }
}

void insert(LinkedList &l) {
    for (int i = 0; i < 10; i++) {
        l.insertElement(i, rand()%100);
    }
}

void del(LinkedList& l) {
    for (int i = 0; i < 10; i++) {
        l.deleteElement();
    }
}

int main() {
    LinkedList list;
    add(lista);

    thread t1(del, ref(list));
    thread t2(del, ref(list));


    t1.join();
    t2.join();

    cout << list;
}
