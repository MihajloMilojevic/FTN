#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#define SIZE 30
#define ST_SIZE 100
void hipotenuza()
{
    float a, b;
    printf("Unesite a i b: ");
    scanf("%f %f", &a, &b);
    printf("Hipotenuza je: %.2f\n", sqrt(a*a + b*b));
}
int ucitaj(int niz[])
{
    int i = 0, n;
    printf("Unesite n: ");
    scanf("%d", &n);

    for(; i < n; i++)
    {
        scanf("%d", &niz[i]);
    }
    return n;
}
int suma(int niz[], int n, bool prompt)
{
    int i = 0, sum = 0;
    for(; i < n; i++)
    {
        sum += niz[i];
    }
    if(prompt)
        printf("Suma niza je %d\n", sum);
    return sum;
}

void ispis(int niz[], int n)
{
    int i = 0;
    printf("Ipsis: \n");
    for(; i < n; i++)
    {
        printf(" %d ", niz[i]);
    }
    printf("\n");
}

void sr_v(int niz[], int n)
{
    int s = suma(niz, n, false);
    printf("Srednja vrednost je: %.2f\n", s*1.0/n);
}

void minel(int niz[], int n)
{
    int i = 0;
    int mini = niz[0];
    for(; i < n; i++)
    {
        if(niz[i] < mini)
            mini = niz[i];
    }
    printf("Najmanji je %d\n", mini);
}
void maxel(int niz[], int n)
{
    int i = 0;
    int maxi = niz[0];
    for(; i < n; i++)
    {
        if(niz[i] > maxi)
            maxi = niz[i];
    }
    printf("Najveci je %d\n", maxi);
}

void zadatak1()
{
    int niz[SIZE];
    int n;
    n = ucitaj(niz);
    suma(niz, n, true);
    ispis(niz, n);
    hipotenuza();
}


void zadatak2()
{
    int niz[SIZE];
    int n;
    n = ucitaj(niz);
    while(1)
    {

        int o;
        printf("Unesite izbor 0:izlaz 1:suma 2:srednja vrednost 3:min el 4:max el\n");
        scanf("%d", &o);
        if(!o)
            break;
        switch(o)
        {
            case 1:
                suma(niz, n, true);
                break;
            case 2:
                sr_v(niz, n);
                break;
            case 3:
                minel(niz, n);
                break;
            case 4:
                maxel(niz, n);
                break;
            default:
                printf("Ne postoji takav izbor!\n");
                break;
        }
    }

}

void zadatak3()
{
    char st[ST_SIZE];
    gets(st);
    int n = strlen(st);
    int oc = 0;
    while(1)
    {
        int o;
        printf("Unesite izbor 0:izlaz 1:ispis 2:obrnuto 3: prebroj karakter 4:duzina stringa 5:velika slova\n");
        scanf("%d", &o);
        if(!o)
            break;
        switch(o)
        {
            case 1:
                puts("Uneti string je: ");
                puts(st);
                break;
            case 2:
                puts("Sa strlen");
                for(int i = n - 1; i >= 0; i--)
                    putchar(st[i]);
                putchar('\n');
                puts("Bez strlen");
                char novi[ST_SIZE];
                int n1 = 0;
                while(st[n1] != '\0') n1++;
                for(int i = n1 - 1; i >= 0; i--)
                    putchar(st[i]);
                putchar('\n');
                break;
            case 3:
                fflush(stdin);
                puts("Unesite karakter za pretragu: ");
                char p;
                scanf("%c", &p);
                oc = 0;
                for(int i = n - 1; i >= 0; i--)
                {
                    if(st[i] == p)oc++;
                }
                printf("Karakter %c se pojavio %d puta\n", p, oc);
                break;
            case 4:
                printf("Duzina stringa je %d\n", strlen(st));
                break;
            case 5:
                oc = 0;
                for(int i = n - 1; i >= 0; i--)
                {
                    if(st[i] >= 'A' && st[i] <= 'Z')oc++;
                }
                printf("Broj velikih slova je %d\n", oc);
                break;
            default:
                printf("Ne postoji takav izbor!\n");
                break;
        }
    }
}

typedef struct tacka
{
    int x;
    int y;
    int z;
} Tacka;

void ucitaj2d(Tacka ravan[], int n)
{
    for(int i = 0; i < n; i++)
    {
        printf("Tacka %d: ", i + 1);
        scanf("%d %d", &ravan[i].x, &ravan[i].y);
        ravan[i].z = 0;
    }
}
void ucitaj3d(Tacka prostor[], int n)
{
    for(int i = 0; i < n; i++)
    {
        printf("Tacka %d: ", i + 1);
        scanf("%d %d %d", &prostor[i].x, &prostor[i].y, &prostor[i].z);
    }
}
void najudaljenija(Tacka ravan[], int n, bool printz)
{
    Tacka t  = ravan[0];
    int maxi = sqrt(t.x*t.x + t.y*t.y + t.z*t.z);
    Tacka najveca;
    for(int i = 0; i < n; i++)
    {
        t = ravan[i];
        double d = sqrt(t.x*t.x + t.y*t.y + t.z*t.z);
        if(d > maxi)
        {
            maxi = d;
            najveca = t;
        }
    }
    if(printz)
        printf("Tacka najdalja od k. pocetka je: (%d, %d, %d)\n", najveca.x, najveca.y, najveca.z);
    else
        printf("Tacka najdalja od k. pocetka je: (%d, %d)\n", najveca.x, najveca.y);

}

void zadatak4()
{
    Tacka ravan[30];
    Tacka prostor[30];
    int n1, n2;
    puts("Unesite koliko tacaka zelite u ravni: ");
    scanf("%d", &n1);
    ucitaj2d(ravan, n1);
    puts("Unesite koliko tacaka zelite u prostoru: ");
    scanf("%d", &n2);
    ucitaj3d(prostor, n2);
    najudaljenija(ravan, n1, false);
    najudaljenija(prostor, n2, true);
}




int main()
{
    //zadatak1();
    //zadatak2();
    //zadatak3();
    zadatak4();
    return 0;
}
