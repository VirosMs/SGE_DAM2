"""
2. Escribir un programa que pida al usuario una palabra y 
muestre por pantalla el número de veces que contiene cada vocal (a,e,i,o,u) y si es un palíndromo o no.
"""

def numVocal():
    palabra = input("Introduce una palabra: ")
    vocales = ['a', 'e', 'i', 'o', 'u']
    if not(palabra == "") and not(palabra == " "):
        for vocal in vocales:
            print(f'La vocal {vocal} aparece {palabra.count(vocal)} veces')
        if palabra == palabra[::-1]:
            print("Es un palíndromo")
        else:
            print("No es un palíndromo")
    else:
        print("No has introducido ninguna palabra")

numVocal()