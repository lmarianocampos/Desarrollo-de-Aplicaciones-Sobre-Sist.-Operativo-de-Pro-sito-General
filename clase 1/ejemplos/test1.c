#include <stdio.h>

#define LEN	10000000

static long numeros[LEN];
static long salida[LEN];

static long calcularCuadrado(long x)
{
	return x*x;
}

int main(void)
{
	long i;
	for(i=0; i<LEN; i++)
		numeros[i]=i;	

	for(i=0; i<LEN; i++)
		salida[i]=calcularCuadrado(numeros[i]);	
	

	return 0;
}

