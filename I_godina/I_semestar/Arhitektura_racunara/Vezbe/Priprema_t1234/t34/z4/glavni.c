#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int prebrojNajviseUzastopnih(unsigned long long* vrednost);

void printbin64(unsigned long long x) {
    unsigned long long m=0x8000000000000000ULL;
    int s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
    printf("\n");
}

int main() {
    unsigned long long v;
    int r;

    printf("Vrednost (hex): ");
    scanf("%llx",&v);
    printf("Binarno: ");
    printbin64(v);
    r = prebrojNajviseUzastopnih(&v);
    printf("Najveci broj uzastopnih nula je %d\n", r);

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return 0;
}
