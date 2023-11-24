#include <stdio.h>
#define N 10

int SetParityArray(unsigned short int* niz, int n);

void printbin16(unsigned short int x) {
    unsigned short int m=0x8000, s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
}

int main() {
    unsigned short int niz[N] = {1,2,3,4,0x8765,0x74af,55,0,0xffff,12345};
    int x,i;
    printf("Ulaz:\n");
    for(i=0;i<N;i++) {
        printf("%2d:",i);
        printbin16(niz[i]);
        printf("\n");
    }
    x = SetParityArray(niz,N);
    printf("Izlaz (broj postavljenih jedinica:%d):\n",x);
    for(i=0;i<N;i++) {
        printf("%2d:",i);
        printbin16(niz[i]);
        printf("\n");
    }
}

