"""
1. Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada signatura y después las muestre por pantalla con el mensaje "En la asignatura <ASIG> has sacado un <NOTA>". 
Debajo que nos muestre la nota media.
"""

def notas():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = []
    for asignatura in asignaturas:
        nota = int(input("¿Qué nota has sacado en " + asignatura + "?"))
        notas.append(nota)
    for i in range(len(asignaturas)):
        print(f'En la asignatura {asignaturas[i]} has sacado un {notas[i]}')
    
    print(f'La nota media es {sum(notas)/len(notas)}')

notas()