#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int SetParity(unsigned short int* v);

void printbin16(unsigned short int x) {
    unsigned short int m=0x8000, s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
    printf(" (%d)",x);
}

int main() {
    unsigned short int v;
    int r=0, g=0;

    printf("Unesite vrednost: ");
    scanf("%hu",&v);
    printf("\nVrednost pre  : ");
    printbin16(v);
    r = SetParity(&v);
    printf("\nVrednost posle: ");
    printbin16(v);
    printf("\nPostavljeni paritet: %d\n",r);

    if (RUNPP_REG_ERR) return RUNPP_REG_ERR+128;
    else return g;
}

