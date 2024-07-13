#include <stdio.h>
#include <stdlib.h>

int mnozenje(int a, int b)
{
    int i = 0;
    int s = 0;
    while(i < b){
        s += a;
        i++;
    }
    return s;
}
int deljenje(int a, int b)
{
    int i = 0;
    while(a > 0)
    {
        a -= b;
        i++;

    }
    return i;
}

int main()
{
    int n;
    scanf("%d", &n);
    int i = 1, sum = 0;
    while(i <= n){
        sum += i;
        i++;
    }
    printf("Suma (1 - %d): %d\n", n, sum);

    printf("Deljenje %d\n", deljenje(10, 5));

    printf("Mnozenje %d\n", mnozenje(3, 5));

    int n1, n2;
    printf("Unesite n1 i n2\n");
    scanf("%d %d", &n1, &n2);
    for(;n1 <= n2; n1++)
    {
        if(n1%2)
            printf("%d\n", n1);
    }

    int q;
    printf("Unesite n i q\n");
    scanf("%d %d", &n, &q);
    i = 2;
    while(i <= n)
    {
        if(!(i%q))
            printf("%d\n", i);
        i++;
    }

    return 0;
}
