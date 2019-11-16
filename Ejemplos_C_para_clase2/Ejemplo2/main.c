#include <stdio.h>
#include "Persona.h"



int main(void)
{
	Persona* p;

	p = per_new();
	if(p!=NULL)
	{
		per_setNombre(p,"Ernesto");
		per_setEdad(p,32);
		per_printPersona(p);
	}

	return 0;
}
