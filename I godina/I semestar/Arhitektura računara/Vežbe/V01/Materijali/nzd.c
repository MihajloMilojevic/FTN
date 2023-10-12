#include <stdio.h>

int main(){

int a=12;
int b=8;

while (a != b)
	if(a > b)
		a -= b;
	else	
		b -= a;

printf("NZD=%d\n",a);
}
