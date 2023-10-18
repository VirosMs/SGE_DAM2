#Author: Charles Arruda Santos

import sys
import timeit

# Crear una lista y una tupla con el mismo contenido
mylist=[1, 3, 4, 5,"hello",True]
mytuple=(1, 3, 4, 5,"hello",True)

# Medir el tiempo de acceso a un elemento en la lista y en la tupla
def acceso_lista():
    return mylist[3]

def acceso_tupla():
    return mytuple[3]

tiempo_acceso_lista = timeit.timeit(acceso_lista, number=1000000)
tiempo_acceso_tupla = timeit.timeit(acceso_tupla, number=1000000)

# Medir la memoria ocupada por la lista y la tupla
list_size = sys.getsizeof(mylist)
tuple_size = sys.getsizeof(mytuple)

# Imprimir los resultados
print("Tiempo de acceso a un elemento en la lista: ", tiempo_acceso_lista)
print("Tiempo de acceso a un elemento en la tupla: ", tiempo_acceso_tupla)
print("Tamaño de la lista en memoria: ", list_size)
print("Tamaño de la tupla en memoria: ", tuple_size)
print("----------------------------------------------")


# Medir el tiempo de acceso a los elementos de la lista y unirlos en una cadena utilizando un bucle for y concatenación de cadenas
def unir_list_for():
    my_string = ''
    for element in mylist:
        my_string += element
    return my_string


def unir_tupla_for():
    my_string = ''
    for element in mytuple:
        my_string += element
    return my_string


tiempo_unir_list_for = timeit.timeit(lambda: unir_list_for, number=1000000)
tiempo_unir_tupla_for = timeit.timeit(lambda: unir_tupla_for, number=1000000)
print("Tiempo de acceso y unión de cadenas con un bucle for y concatenación de cadenas utilizando una lista: ", tiempo_unir_list_for)
print("Tiempo de acceso y unión de cadenas con un bucle for y concatenación de cadenas utilizando una tupla: ", tiempo_unir_tupla_for)


print("----------------------------------------------")

# Medir el tiempo de acceso a los elementos de la lista y unirlos en una cadena utilizando el método join()
tiempo_mylist_join = timeit.timeit(lambda: "".join(map(str, mylist)), number=1000000)
tiempo_mytuble_join = timeit.timeit(lambda: "".join(map(str, mytuple)), number=1000000)

print("Tiempo de acceso y unión de cadenas con el método join() utilizando una lista: ", tiempo_mylist_join)
print("Tiempo de acceso y unión de cadenas con el método join() utilizando una tupla: ", tiempo_mytuble_join)
