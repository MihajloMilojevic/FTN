#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct elem
{
    int broj;
    int godina;
    char marka[11];
    struct elem *sled;

} Elem;

Elem *na_pocetak(Elem *lista, int b);
Elem *na_kraj(Elem *novi, Elem *lst);
void brisiSve(Elem *lst);
void pisi(Elem *lst);
Elem *brisiElement(Elem *lst, int b);
void brisiSve(Elem *lst);
Elem *umetni(Elem *lst, int b);


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

Elem* ucitaj_automobile(Elem* glava, FILE* in)
{

    int i = 0, kubikaza, godiste;
    char marka[11];
    while(fscanf(in, "%s %d %d", marka, &kubikaza, &godiste) == 3)
    {
        Elem* novi = (Elem*)malloc(sizeof(Elem));
        strcpy(novi->marka, marka);
        novi->broj = kubikaza;
        novi->godina = godiste;
        glava = na_kraj(novi, glava);
    }
    return glava;
}

void najnovije(Elem* lst, int min_kubikaza)
{
    if(!lst)
        return;
    Elem* najbolji = NULL;
    while (lst)
    {
        if(lst->broj > min_kubikaza)
        {
            if(najbolji == NULL || lst->godina > najbolji->godina)
            {
                najbolji = lst;
            }

        }
        lst = lst -> sled;
    }
    printf("\nNajbolji za minimalnu kubikazu od %d je: %s %d %d \n", min_kubikaza, najbolji->marka, najbolji->broj, najbolji->godina);
}

int main(int argnum, char *args[])
{
    Elem* glava = NULL;
    if(argnum != 3)
    {
        exit(1);
    }
    char *in_filename = args[1];
    int min_kubikaza = atoi(args[2]);

    FILE *in = safe_fopen(in_filename, "r", 2);
    glava = ucitaj_automobile(glava, in);
    pisi(glava);
    najnovije(glava, min_kubikaza);
    return 0;
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

Elem *na_pocetak(Elem *lista, int b)
{
        Elem *novi = (Elem*)malloc(sizeof(Elem));
        novi->broj = b;
        novi->sled = lista;
        lista = novi;
        return lista;
}

void pisi(Elem *lst) {
    if(!lst)
        return;
    while (lst->sled)
    {
        printf("%s %d %d ; ", lst->marka, lst->broj, lst->godina);
        lst = lst -> sled;
    }
    printf("%s %d %d \n", lst->marka, lst->broj, lst->godina);
}

Elem *brisiElement(Elem *lst, int b){
    Elem *tek = lst;
    Elem *pret = NULL;
    while (tek)
    {
        if (tek->broj != b)
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

void brisiSve(Elem *lst) {
    while (lst)
    {
        Elem *stari = lst;
        lst = lst->sled;
        free(stari);
    }
}

Elem *umetni(Elem *lst, int b) {
    Elem *tek=lst;
    Elem *pret=NULL;
    while (tek && tek->broj < b)
    {
        pret = tek;
        tek = tek->sled;
    }
    Elem *novi = malloc(sizeof(Elem));
    novi->broj = b;
    novi->sled = tek;
    if (!pret)
    {
        lst = novi;
    }
    else
    {
        pret->sled = novi;
    }
    return lst;
}
