import sys
from itertools import zip_longest

def main():
    if len(sys.argv) < 3:
        print(f"Uso: {sys.argv[0]} nombre_archivo")
        return 1

    with open(sys.argv[1], 'r', encoding="utf-8") as archivo:
        texto = archivo.read()
        
    apariciones = {} #Para conteos

    # Recorrer el texto y contar las apariciones de cada letra
    for letra in texto:
        if letra.isalpha():  # Esto cuenta solo letras
            letra = letra.lower()  # Convertir a minúscula
            if letra in apariciones: 
                apariciones[letra] += 1 # para acceder o modificar el valor asociado a esa letra.
            else: 
                apariciones[letra] = 1
                
    
    # lista_apariciones = [(letra, contador) for letra, contador in apariciones.items()]
    
    # Ordenar la lista por apariciones en orden descendente y convertir el diccionario en una lista de tuplas (letra, apariciones)
    lista_apariciones = sorted(apariciones.items(), key=lambda x: x[1], reverse=True)
    
    
    # === Archivo 2: frecuencias ===
    lista_freq = []
    with open(sys.argv[2], 'r', encoding="utf-8") as archivo_freq:
        for linea in archivo_freq:
            partes = linea.strip().split() # Elimina los espacios al principio y final de la línea.split() separa la línea en partes
            if len(partes) == 2:
                letra, valor = partes #Asigna los dos elementos de la lista partes a variables
                try:
                    valor = float(valor.replace(",", "."))
                    lista_freq.append((letra.lower(), valor))
                except ValueError:
                    continue

    # === Combinar como columnas ===
    print("Letra1\tApariciones\tLetra2\tFrecuencia")
    for (letra1, apar), (letra2, freq) in zip_longest(lista_apariciones, lista_freq, fillvalue=("-", 0)):
        print(f"{letra1}\t{apar}\t\t{letra2}\t{freq}")

if __name__ == "__main__":
    main()

