#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int prebrojPalindrome(unsigned long long* niz, int n);

#define MAXLEN 20
unsigned long long a[MAXLEN];

int unesi_niz(char ime, unsigned long long *niz, int n) {
    int i;
    printf("\nUnesite elemente niza '%c'\n",ime);
    for (i=0;i<n;i++) {
        printf("%c[%d]=",ime,i);
        scanf("%llu",&niz[i]);
    }
}

void printbin64(unsigned long long x) {
    unsigned long long m=0x8000000000000000ULL;
    int s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
}

int print_niz64(char ime, unsigned long long *niz, int n) {
    int i;
    printf("\nElementi niza '%c'\n",ime);
    for (i=0;i<n;i++) {
        printbin64(niz[i]);
        printf("\n");
    }   
}

int main() {
    int n, r;
    printf("Unesite N: ");
    scanf("%d",&n);
    
    unesi_niz('a',a,n);
    print_niz64('a', a, n);
    
    r = prebrojPalindrome(a, n);    
    printf("\n\nBroj palindroma u prosledjenom nizu je: %d.\n", r);

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return 0;
}
