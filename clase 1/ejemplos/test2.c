#include <stdio.h>
#include <string.h>
#include <stdlib.h>


#define LEN	1000000

struct S_Usuario{

	char* pNombre;
	int dni;
};
typedef struct S_Usuario Usuario;

static Usuario* users[LEN];

static Usuario* newUser(char* pName, int dni)
{
	Usuario* pU;
	pU = (Usuario*)malloc(sizeof(Usuario));
	if(pU!=NULL)
	{
		pU->pNombre = malloc(strlen(pName)+1);
		if(pU->pNombre!=NULL)
			strcpy(pU->pNombre,pName);
		pU->dni = dni;
	}
	return pU;
}

int main(void)
{
	long i;
	for(i=0; i<LEN; i++)
		users[i]=newUser("Ernesto",33263106);	

	
	return 0;
}
