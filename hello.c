/* Inclusion de bibliotecas */
#include <stdio.h>

/* Programa principal */
int main(int argc, char *argv[]) {

	if(argc < 2) {
		printf("Uso: ./hello [nombre]");
		return 1;
	}
	/* TODO */
	printf("Hola %s!", argv[1]);

	/* Fin del programa */
	return 0;
}
