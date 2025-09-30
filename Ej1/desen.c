#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Uso: %s nombre_archivo\n", argv[0]);
        return 1;
    }
    
    char letras[27];
    int apariciones[27] = {0};
    float probabilidades[27] = {0};
    char letrasO[27] = {'E','A','O','L','S','N','D','R','U','I','T','C','P','M','Y','Q','B','H','G','F','V','J','Ñ','Z','X','K','W'};
    int x;
    FILE *ftexto;
    int cont = 0;
    
    for (int i = 0; i < 26; i++) {
        letras[i] = 'A' + i;
    }
    
    ftexto= fopen(argv[1], "r");
    if (!ftexto)
    { printf("El archivo %s no existe\n",argv[1]);
        return 1;
    }
    
    while ((x = fgetc(ftexto)) != EOF) {
        x = toupper(x);                // Convierte a mayúscula
        if (x >= 'A' && x <= 'Z') {
            apariciones[x - 'A'] += 1;
            letras[x - 'A'] = x;
            cont++;
        }
    }
    fclose (ftexto);
    for (int i = 0; i < 26 - 1; i++) {
      for (int j = i + 1; j < 26; j++) {
        if (apariciones[i] < apariciones[j]) {
            // Intercambiar apariciones
            int temp = apariciones[i];
            apariciones[i] = apariciones[j];
            apariciones[j] = temp;

            // Intercambiar letras en paralelo
            char tempc = letras[i];
            letras[i] = letras[j];
            letras[j] = tempc;
        }
      }
    }
    for (int i = 0; i < 26; i++) {
        if (cont > 0)
            probabilidades[i] = (float)apariciones[i] / cont; //Hacemos el casting
    }
    
    ftexto= fopen(argv[1], "r");
    FILE *fsalida = fopen("resultado.txt", "w");
    if (fsalida) {
        while ((x = fgetc(ftexto)) != EOF) {
          x = toupper(x);                // Convierte a mayúscula
          if (x >= 'A' && x <= 'Z') {
            for (int j = 0; j < 26; j++) {
              if (letras[j] == x) {
                fprintf(fsalida, "%c", letrasO[j]);
                break;
              }
            }
          } else {
            fprintf(fsalida, "%c", x);
          }
        }
    }
    printf("Letra\tApariciones\tProbabilidad\tSustituidaPor\n");
    for (int i = 0; i < 26; i++) {
        printf("%c\t%d\t\t%.4f\t\t%c\n",
               letras[i], apariciones[i], probabilidades[i], letrasO[i]);
    }

    fclose(fsalida);
    fclose (ftexto);
    return 0;
}
