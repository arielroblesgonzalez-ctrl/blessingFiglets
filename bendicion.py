#!/usr/bin/env python3
"""
Script que convierte texto en arte ASCII tipo FIGlet.
Uso: python bendicion.py "Tu frase aqui"
Si no pasas argumento, usa "Dios te bendiga!" por defecto.
"""

import sys
import pyfiglet


def main():
    # Tomar la frase del argumento de linea de comandos o usar el valor por defecto
    if len(sys.argv) > 1:
        frase = " ".join(sys.argv[1:])
    else:
        frase = "Dios te bendiga!"

    # Crear el objeto Figlet con una fuente llamativa
    fig = pyfiglet.Figlet(font='slant')

    # Generar el arte ASCII
    arte = fig.renderText(frase)

    # Imprimir con un borde decorativo
    ancho = max(len(linea) for linea in arte.split('\n')) if arte else 0
    borde = '+' + '-' * (ancho + 2) + '+'

    print()
    print(borde)
    for linea in arte.split('\n'):
        print(f"| {linea:<{ancho}} |")
    print(borde)
    print()


if __name__ == "__main__":
    main()
