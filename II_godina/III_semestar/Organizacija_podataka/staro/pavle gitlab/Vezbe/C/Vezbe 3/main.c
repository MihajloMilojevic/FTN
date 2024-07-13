#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct student{
    int indeks;
    int godina;
    char ime[30];
    char prezime[30];

} Student;

Student ucitajStudenta()
{
    Student s;
    scanf("%d\n%d", &s.indeks, &s.godina);
    fflush(stdin);
    gets(s.ime);
    gets(s.prezime);
    return s;
}

void stampajStudenta(Student s)
{
    printf(" %d %d %s %s ", s.indeks, s.godina, s.ime, s.prezime);
}

void anulirajStudenta(Student *s)
{
    char *n = "0";
    s->godina = 0;
    s->indeks = 0;
    strcpy(s->ime, n);
    strcpy(s->prezime, n);

}

Student *ucitaj(int n)
{
    Student *niz = (Student*)malloc(sizeof(Student)*n);
    for(int i = 0; i < n; i++)
    {
        printf("Unesite el. br %d:  \n", i + 1);
        printf("Indeks, godina, ime, prezime\n");
        niz[i] = ucitajStudenta();
    }
    for(int i = 0; i < n; i++)
        stampajStudenta(niz[i]);
    printf("\n");
    return niz;
}

Student *prosiri(int n, int k, Student *niz)
{
    Student *novi = (Student*)malloc(sizeof(Student)*(n + k));
    for(int i = 0; i < n; i++)
        novi[i] = niz[i];

    for(int i = n; i < n + k; i++)
    {
        printf("Unesite el. br %d:  ", i + 1);
        printf("Indeks, godina, ime, prezime\n");
        novi[i] = ucitajStudenta();
    }
    for(int i = 0; i < n + k; i++)
        stampajStudenta(novi[i]);
    printf("\n");
    free(niz);
    return novi;
}

void anuliraj(int n, Student *niz)
{
    for(int i = 0; i < n; i++)
    {
        anulirajStudenta(&niz[i]);
    }
    for(int i = 0; i < n; i++)
        stampajStudenta(niz[i]);
    printf("\n");
}

void zadatak1()
{
    int n, k, o = 1;
    printf("Uneti n: ");
    scanf("%d", &n);
    Student *niz = ucitaj(n);
    while(o)
    {
        printf("Unesite 0 za izlaz, 1 za prosirivanje i 2 za anuliranje: ");
        scanf("%d", &o);
        switch(o)
        {
        case 0:
            break;
        case 1:
            printf("Uneti k: ");
            scanf("%d", &k);
            niz = prosiri(n, k, niz);
            n = n + k;
            break;
        case 2:
            anuliraj(n, niz);
            break;
        }

    }
    free(niz);
}


void zadatak2()
{
    int n;
    printf("Unesite n: ");
    scanf("%d", &n);
    int *niz = (int*)malloc(sizeof(int)*n);
    for(int i = 0; i < n; i++)
    {
        printf("Unesite %d broj: \n", i);
        scanf("%d", &niz[i]);
    }

    FILE *fp = fopen("naz.txt", "w");
    if(fp == NULL)
    {
        printf("Greska pri otvaranju\n");
        return;
    }
    for(int i = 0; i < n; i++)
    {
        fprintf(fp, "%d %d\n", niz[i], niz[i]*niz[i]);
    }

    if(fclose(fp) == EOF)
    {
        printf("Greska pri zatvaranju\n");
        return;
    }
}

void zadatak3()
{
    int n;
    printf("Unesite n: ");
    scanf("%d", &n);
    int *niz = (int*)malloc(sizeof(int)*2*n);
    n = 2*n;
    for(int i = 0; i < n; i+=2)
    {
        printf("Unesite broj: \n");
        scanf("%d", &niz[i]);
        niz[i+1] = niz[i]*niz[i];
    }

    FILE *fp = fopen("naz.bin", "w");
    if(fp == NULL)
    {
        printf("Greska pri otvaranju\n");
        return;
    }

    fwrite(niz, sizeof(int), n, fp);
    if(fclose(fp) == EOF)
    {
        printf("Greska pri zatvaranju\n");
        return;
    }

    fp = fopen("naz.bin", "r");
    int *niz2 = (int*)malloc(sizeof(int)*n);
    fread(niz2, sizeof(int), n, fp);
    for(int i = 0; i < n; i++)
        printf("%d ", niz2[i]);
    fclose(fp);
}
///
typedef struct student2
{
    int indeks;
    char ime[30];
    int ocene[30];
    float prosek;
    int br_ocena;

} Student2;
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

void unos_niza(FILE *in, Student2 *niz, int *n)
{
    int i = 0, indeks, ocena;
    char ime[30];
    while(fscanf(in, "%d %s %d", &indeks, ime, &ocena) == 3)
    {
        int novi = 1;
        for(int j = 0; j < (*n); j++)
        {
            if(strcmp(niz[j].ime, ime) == 0 && niz[j].indeks == indeks)
            {
                niz[j].ocene[niz[j].br_ocena] = ocena;
                niz[j].prosek = (niz[j].prosek*niz[j].br_ocena + ocena)/(niz[j].br_ocena + 1);
                niz[j].br_ocena++;
                novi = 0;
            }
        }
        if(novi)
        {
            Student2 nst;
            strcpy(nst.ime, ime);
            nst.indeks = indeks;
            nst.ocene[0] = ocena;
            nst.br_ocena = 1;
            nst.prosek = (float)ocena;
            niz[(*n)] = nst;
            (*n)++;
        }
    }
}

void ispis_niza(FILE *out, Student2 *niz, int n)
{
    int i;
    for(i = 0; i < n; i++)
    {
        ispis_studenta(out, niz[i]);
    }
}
void ispis_studenta(FILE *out, Student2 a)
{
    fprintf(out, "%d %s %f\n", a.indeks, a.ime, a.prosek);
}

void ispis_najb(FILE *out, Student2 *niz, int n)
{
    int i;
    Student2 naj;
    float np = -1;
    for(i = 0; i < n; i++)
    {
        if(niz[i].prosek > np)
        {
            np = niz[i].prosek;
            naj = niz[i];
        }
    }
    ispis_studenta(out, naj);
}

void ispis_najg(FILE *out, Student2 *niz, int n)
{
    int i;
    Student2 naj;
    float np = 1000;
    for(i = 0; i < n; i++)
    {
        if(niz[i].prosek < np)
        {
            np = niz[i].prosek;
            naj = niz[i];
        }
    }
    ispis_studenta(out, naj);
}


int main(int argnum, char *args[])
{
    //zadatak1();
    //zadatak2();
    //zadatak3();

    if(argnum != 4)
    {
        exit(1);
    }
    char *in_filename = "studenti.txt";
    char *out1_filename = args[2];
    char *out2_filename = args[3];

    Student2 niz[50];

    FILE *in = safe_fopen(in_filename, "r", 2);
    FILE *out1 = safe_fopen(out1_filename, "w", 3);
    FILE *out2 = safe_fopen(out2_filename, "w", 3);
    int p = 0;
    int n = 0;
    printf("%d ", n);
    unos_niza(in, niz, &n);
    for(int i = 0; i < (n); i++)
        printf(" %d %s %d ;", niz[i].indeks, niz[i].ime, niz[i].br_ocena);
    ispis_najb(out1, niz, n);
    ispis_najg(out2, niz, n);

    fclose(in);
    fclose(out1);
    fclose(out2);

    return 0;
}
