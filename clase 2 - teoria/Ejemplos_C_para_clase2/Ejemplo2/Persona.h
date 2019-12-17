struct S_Persona
{
	char nombre[20];
	int edad;
};
typedef struct S_Persona Persona;


void per_setEdad(Persona* p,int edad);
void per_setNombre(Persona* p,char* nombre);
void per_printPersona(Persona* p);
Persona* per_new(void);

