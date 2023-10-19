#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

unsigned int maska(unsigned int n, unsigned int v);

void printbin(unsigned int x) {
    unsigned int m=0x80000000, s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%4 ? "" : "");
        m >>= 1;
    }
}

int main() {
    unsigned int n, v, r=0, g=0;

    printf("Unesite N: ");
    scanf("%d",&n);
    printf("Unesite V: ");
    scanf("%d",&v);
    printf("Maska: ");
    r = maska(n,v);
    printbin(r);
    printf("\n");

    if (RUNPP_REG_ERR) return RUNPP_REG_ERR+128;
    else return g;
}

