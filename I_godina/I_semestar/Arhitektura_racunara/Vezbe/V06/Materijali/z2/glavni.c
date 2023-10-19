#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

unsigned long long maska64(unsigned int n, unsigned int v);

void printbin64(unsigned long long x) {
    unsigned long long m=0x8000000000000000ULL;
    int s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
}

int main() {
    unsigned int n, v, g=0;
    unsigned long long r;

    printf("Unesite N: ");
    scanf("%d",&n);
    printf("Unesite V: ");
    scanf("%d",&v);
    printf("Maska: ");
    r = maska64(n,v);
    printbin64(r);
    printf("\n");

    if (RUNPP_REG_ERR) return RUNPP_REG_ERR+128;
    else return g;
}

