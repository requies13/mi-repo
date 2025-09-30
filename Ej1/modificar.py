import sys

def main():
    # Verificar si se proporcionaron los parámetros correctos
    if len(sys.argv) < 4:
        print("Uso: python3 modificar_texto.py nombre_archivo <letra_a_cambiar> <letra_a_reemplazar>")
        return 1

    archivo_nombre = sys.argv[1]
    letra_a_cambiar = sys.argv[2]
    letra_a_reemplazar = sys.argv[3]

    # Leer el contenido actual del archivo de texto
    with open(archivo_nombre, 'r', encoding="utf-8") as archivo:
        texto = archivo.read()

    # Realizar el reemplazo de la letra
    texto_modificado = texto.replace(letra_a_cambiar.upper(), letra_a_reemplazar)

    # Escribir el texto modificado de nuevo en el archivo
    with open(archivo_nombre, 'w', encoding="utf-8") as archivo:
        archivo.write(texto_modificado)

    print(f'Se ha cambiado la letra "{letra_a_cambiar.upper()}" por "{letra_a_reemplazar}" en el archivo "{archivo_nombre}".')
    return 0

if __name__ == "__main__":
    main()

