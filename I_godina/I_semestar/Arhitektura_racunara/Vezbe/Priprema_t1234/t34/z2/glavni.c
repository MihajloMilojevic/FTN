#include <stdio.h>

#define MAX 32

unsigned int RUNPP_REG_ERR = 0;

int InvertBits(unsigned int* indeksi, int n);

void printbin(unsigned int x) {
    unsigned int m=0x80000000, s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
}

int main() {
    unsigned int v, g=0;
    int r, duzina_niza, niz[MAX];
    
    printf("Unesite duzinu niza (maksimalno %d): ", MAX);
    scanf("%d", &duzina_niza);

    printf("Unesite elemente niza u decimalnom zapisu:\n");
    for (int i = 0; i < duzina_niza; i++) {
        printf("niz[%d]=", i);
        scanf("%d", &niz[i]);
    } printf("\n");

    r = InvertBits(niz, duzina_niza);

    printf("\nIzlaz: ");
    printbin(r);
    printf("\n");

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n", RUNPP_REG_ERR);
    #endif
    return g;
}

