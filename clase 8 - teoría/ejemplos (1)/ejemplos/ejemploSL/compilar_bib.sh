gcc -c -Wall -Werror -fpic biblioteca.c
gcc -shared -o libbiblioteca.so biblioteca.o
