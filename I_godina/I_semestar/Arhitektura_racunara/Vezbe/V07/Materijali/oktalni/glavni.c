#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

unsigned int inter_to_oct_str(unsigned int broj, char* str, unsigned int duzina);

int main() {
    unsigned int broj,duzina;
    char s[30];
    unsigned int g;
    printf("Unesite dekadni 32-bitni broj:");
    scanf("%u",&broj);
    printf("Unesite duzinu bafera:");
    scanf("%u",&duzina);
    g = inter_to_oct_str(broj,s,duzina);
    printf("Greska: %u\n",g);
    if (g == 0)
        printf("String: %s\n",s);
    printf("\n");

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return ((g<0)||(g>127))?127:g;
}

