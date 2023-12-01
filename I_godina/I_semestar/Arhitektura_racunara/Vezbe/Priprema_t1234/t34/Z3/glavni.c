#include<stdio.h>

unsigned int Zadatak(unsigned int l, unsigned int r);

void printbin(unsigned int x) {
    unsigned int m=0x80000000, s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
}

int main(){

    unsigned int l, r;
    printf("Unesi broj nula sa leve strane: ");
    scanf("%u", &l);

    printf("Unesi broj nula sa desne strane: ");
    scanf("%u", &r);

    unsigned int rez = Zadatak(l, r);

    printf("Rezultat je: ");
    printbin(rez);
    printf("\n");

    return 0;
}