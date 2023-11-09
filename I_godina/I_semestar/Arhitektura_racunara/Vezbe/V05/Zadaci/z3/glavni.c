#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int saberi_niz(long long *a, long long *b, long long *c, int n);

#define MAXLEN 20
long long a[MAXLEN], b[MAXLEN], r[MAXLEN];

int unesi_niz(char ime, long long *niz, int n) {
    int i;
    printf("\nUnseite elemente niza '%c'\n",ime);
    for (i=0;i<n;i++) {
        printf("%c[%d]=",ime,i);
        scanf("%lld",&niz[i]);
    }
}

int print_niz(char ime, long long *niz, int n) {
    int i;
    printf("\nElementi niza '%c'\n",ime);
    for (i=0;i<n;i++)
        printf("%c[%d]=%lld\n",ime,i,niz[i]);
}

int main()
{
    int g,n;
    printf("Unesite N: ");
    scanf("%d",&n);
    unesi_niz('a',a,n);
    unesi_niz('b',b,n);
    g = saberi_niz(a,b,r,n);
    if (g == 0)
        print_niz('r',r,n);
    else
        printf("Došlo je do greške!\n");
    return g;
}

