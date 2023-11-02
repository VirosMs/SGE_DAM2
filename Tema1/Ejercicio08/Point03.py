

try:
    r = 34/0
except ZeroDivisionError:
    print("Error: división por cero")
    r = 0


try:
    patata= 5 +'Enter number:'
except TypeError:
    print("Error: no se puede sumar un entero y una cadena")
    patata = 0