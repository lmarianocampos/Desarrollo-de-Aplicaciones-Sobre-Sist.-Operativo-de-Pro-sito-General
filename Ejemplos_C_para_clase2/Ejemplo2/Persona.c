#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Persona.h"


Persona* per_new(void)
{
	return (Persona*)malloc(sizeof(Persona));
}


void per_setEdad(Persona* p,int edad)
{
	if(edad<=99)
		p->edad=edad;
}


void per_setNombre(Persona* p,char* nombre)
{
	strncpy(p->nombre,nombre,sizeof(p->nombre));
}


void per_printPersona(Persona* p)
{
	printf("%s edad:%d\r\n",p->nombre,p->edad);
}






