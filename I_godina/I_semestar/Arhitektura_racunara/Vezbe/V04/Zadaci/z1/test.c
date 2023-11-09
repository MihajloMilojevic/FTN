#include<stdio.h>
#include<ctype.h>
#include<string.h>

int main() {
    char ime[40];
    printf("Unesite ime i prezime: \0");
    gets(ime);
    int n = strlen(ime);
    for(int i = 0; i < n; i++) {
        ime[i] = toupper(ime[i]);
    }
    printf("Vi ste: \0");
    printf("%s\n", ime);
    return 0;
}