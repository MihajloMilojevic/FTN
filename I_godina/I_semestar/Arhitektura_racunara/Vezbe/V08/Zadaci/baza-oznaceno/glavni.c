#include <stdio.h>
#include <string.h>

unsigned int RUNPP_REG_ERR = 0;

int str_to_inter(char* str, unsigned int* greska, unsigned int baza);

int main() {
    int r;
    char s[30]={0};
    unsigned int g;
    unsigned int baza;
    printf("Unesite broj u oktalnoj osnovi:");
    scanf("%30[^\n]s",s);
    printf("Unesite bazu (2-32):");
    scanf("%d",&baza);
    r = str_to_inter(s,&g,baza);
    printf("Greska: %u\n",g);
    if (g == 0)
        printf("Rezultat: %d\n",r);
    printf("\n");

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return ((g<0)||(g>127))?127:g;
}

