#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct elem
{
    char ime[21];
    char prezime[21];
    char indeks[11];
    int godina;
    struct elem *sled;

} Elem;
Elem *na_kraj(Elem *novi, Elem *lst);

Elem *na_pocetak(Elem *novi, Elem *lista);

void snimi(Elem* glava, FILE *out);

Elem* ucitaj_studente(Elem* glava, FILE* in);

Elem *brisiElement(Elem *lst, char indeks[11]);

void brisiSve(Elem *lst);

FILE *safe_fopen(char *filename, char *mode, int exit_code)
{
    FILE *f = fopen(filename, mode);
    if(f == NULL)
    {
        printf("Error pri otvaranju\n");
        exit(exit_code);
    }
    return f;
}
Elem* ucitaj_studenta()
{
    char indeks[11];
    char ime[21];
    char prezime[21];
    int upis;
    printf("Unesite indeks: ");
    scanf("%s", indeks);
    printf("Unesite ime: ");
    scanf("%s", ime);
    printf("Unesite prezime: ");
    scanf("%s", prezime);
    printf("Unesite godinu upisa: ");
    scanf("%d", &upis);
    Elem* novi = (Elem*)malloc(sizeof(Elem));
    strcpy(novi->ime, ime);
    strcpy(novi->prezime, prezime);
    strcpy(novi->indeks, indeks);
    novi->godina = upis;
    return novi;
}


void meni(Elem* glava, char* in_filename)
{
    FILE *out;
    FILE *in;
    char indeks[11];
    char ime[21];
    char prezime[21];
    int upis;
    int n = 0, broj;
    Elem *novi;
    do
    {
        printf("Izaberite opciju: \n 1. Dodavanje na pocetak\n 2. Dodavanje na kraj\n 3. Ipsis \n 4. Brisanje elem \n 5. Brisanje svega \n 6. Snimi \n 7. Ucitaj iz datoteke \n 0. Izlaz \n");
        scanf("%d", &n);
        switch(n)
        {
        case 0:
            brisiSve(glava);
            break;
        case 1:
            novi = ucitaj_studenta();
            glava = na_pocetak(novi, glava);
            break;
        case 2:
            novi = ucitaj_studenta();
            glava = na_kraj(novi, glava);
            break;
        case 3:
            printf("Ispis: \n");
            pisi(glava);
            break;
        case 4:
            printf("Unesite indeks: ");
            scanf("%s", &indeks);
            glava = brisiElement(glava, indeks);
            break;
        case 5:
            brisiSve(glava);
            glava = NULL;
            break;
        case 6:
            out = safe_fopen(in_filename, "w", 3);
            snimi(glava, out);
            fclose(out);
            printf("Snimljeno!\n");
            break;
        case 7:
            in = safe_fopen(in_filename, "r", 2);
            brisiSve(glava);
            glava = NULL;
            glava = ucitaj_studente(glava, in);
            fclose(in);
            printf("Ucitano!\n");
            break;
        default:
            printf("Pogresan unos!");
            break;
        }
    }while(n != 0);
}

Elem* ucitaj_studente(Elem* glava, FILE* in)
{
    char ime[21];
    char prezime[21];
    char indeks[11];
    int godina;
    while(fscanf(in, "%s %s %s %d", indeks, ime, prezime, &godina) == 4)
    {
        Elem* novi = (Elem*)malloc(sizeof(Elem));
        strcpy(novi->ime, ime);
        strcpy(novi->prezime, prezime);
        strcpy(novi->indeks, indeks);
        novi->godina = godina;
        glava = na_kraj(novi, glava);
    }
    return glava;
}

int main(int argnum, char *args[])
{
    Elem* glava = NULL;
    if(argnum != 2)
    {
        exit(1);
    }
    char *in_filename = args[1];
    meni(glava, in_filename);
    return 0;
}

void pisi(Elem *lst) {
    if(!lst)
        return;
    while (lst->sled)
    {
        printf("%s %s %s %d ; ", lst->indeks, lst->ime, lst->prezime, lst->godina);
        lst = lst -> sled;
    }
    printf("%s %s %s %d \n \n", lst->indeks, lst->ime, lst->prezime, lst->godina);
}

Elem *na_kraj(Elem *novi, Elem *lst) {
    if (!lst)
    {
        return novi;
    }
    else
    {
        Elem *tek = lst;
        while (tek->sled){
            tek = tek->sled;
        }
        tek->sled = novi;
        return lst;
    }
}

Elem *na_pocetak(Elem *novi, Elem *lista)
{
        novi->sled = lista;
        lista = novi;
        return lista;
}

void snimi(Elem* lst, FILE *out)
{
    while(lst)
    {
        printf("%s %s %s %d\n", lst->indeks, lst->ime, lst->prezime, lst->godina);
        fprintf(out, "%s %s %s %d\n", lst->indeks, lst->ime, lst->prezime, lst->godina);
        printf("Ispisan!\n");
        lst = lst->sled;
    }
    printf("\n\n");

}

void brisiSve(Elem *lst) {
    while(lst)
    {
        Elem *stari = lst;
        lst = lst->sled;
        free(stari);
    }
}


Elem *brisiElement(Elem *lst, char indeks[11]){
    Elem *tek = lst;
    Elem *pret = NULL;
    while (tek)
    {
        if (strcmp(tek->indeks, indeks) != 0)
        {
            pret = tek;
            tek = tek->sled;
        }
        else
        {
            Elem *stari = tek;
            tek = tek->sled;
            if (!pret)
            {
                lst = tek;
            }
            else
            {
                pret->sled = tek;
            }
            free(stari);
        }
    }
    return lst;
}
