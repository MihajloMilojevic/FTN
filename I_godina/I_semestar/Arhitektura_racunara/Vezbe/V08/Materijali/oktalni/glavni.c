#include <stdio.h>
#include <string.h>

unsigned int RUNPP_REG_ERR = 0;

unsigned int oct_str_to_inter(char* str, unsigned int* greska);

int main() {
    unsigned int r;
    char s[30]={0};
    unsigned int g;
    printf("Unesite broj u oktalnoj osnovi:");
    scanf("%30[^\n]s",s);
    r = oct_str_to_inter(s,&g);
    printf("Greska: %u\n",g);
    if (g == 0)
        printf("Rezultat: %u\n",r);
    printf("\n");

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return ((g<0)||(g>127))?127:g;
}

