'''
    1. Escribir un programa que lea tres notas de un alumno y calcule la media de las tres.
    El programa escribirá la media.
    
'''
def ejercicio01():
    n1 = float(input("Ingrese la nota del primero aluno: "))
    n2 = float(input("Ingrese la nota del segundo aluno: "))
    n3 = float(input("Ingrese la nota del tercero aluno: "))

    p = (n1 + n2 + n3) / 3

    print(round(p, 2))


'''
    2. Escribir un programa que lea la base y la altura de un rectángulo y escriba su superficie y su perímetro.
'''
def ejercicio02():
    base = float(input("Ingrese la BASE del rectángulo: "))
    alto = float(input("Ingrese el ALTO del rectángulo: "))

    sup = base * alto

    per = 2 * (base + alto)

    print(f'La superfice del rectángulo es: {sup}')
    print(f'El perímetro del rectángulo es: {per}')


'''
    3. Escribir un programa que lea dos números y muestre cuál es el valor menor de los dos.
'''
def ejercicio03():
    x = int(input("Ingrese el primero numero: "))
    y = int(input("Ingrese el segundo numero: "))

    if x > y:
        print(f'El menor es el segundo numero, con el valor: {y}')
    else:
        print(f'El menor es el primero numero, con el valor: {x}')


'''
    4. Escribir un programa que lea un año indicar si es bisiesto.
    Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
    excepto que también sea divisible por 400.
'''
def ejercicio04():
    anio = int(input("Ingrese el año: "))

    if (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0):
        print("El año es BISIESTO")
    else:
        print("El año NO es BISIESTO")


'''
    5. Escribir un programa que lea tres números y los visualice ordenados de menor a mayor.
    Resolverlo mediante un if-elif-else.
'''
def ejercicio05():
    a = int(2)
    b = int(90)
    c = int(45)

    if a > b:
        if a > c:
            if b > c:
                print(f'{a}, {b}, {c}')
            else:
                print(f'{a}, {c}, {b}')
        else:
            print(f'{c}, {a}, {b}')
    else:
        if b > c:
            if a > c:
                print(f'{b}, {a}, {c}')
            else:
                print(f'{b}, {c}, {a}')
        else:
            print(f'{c}, {b}, {a}')


'''
    6. Escribir un programa que calcule el capital final de una inversión a interés compuesto.
    El usuario debe introducir el capital inicial, el interés anual y el número de años.
'''
def ejercicio06():
    c = -1
    i = -1
    m = -1

    while (c < 0) and ((i <= 0) or (i > 100)) and (m <= 0):
        c = float(input("Escribe el capital inicial: "))
        i = float(input("Escribe el interes anual: "))
        m = float(input("Introduz la cantidad de años: "))

    for j in range(int(m)):
        c *= (1 + i / 100)

    print(f'Tines {round(c, 2)} soles')


'''
    7. Escribir un programa que calcule el valor de e^x mediante la siguiente serie:
    e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + ... + x^n/n!
    El usuario debe introducir el valor de x y el número de términos a calcular (n).
'''
def ejercicio07():
    x = float(input("Introduce el valor de x: "))
    e = float(1)
    num = float(1)
    den = float(1)
    i = float(1)

    num *= x
    den *= i
    i += 1
    e += num/den

    while not((num/den) < 0.000001):
        num *= x
        den *= i
        i += 1
        e += num/den

    print(f'e elevado a {x} es {e}')


'''
    8. Escribir un programa que visualice los cubos de los 20 primeros números naturales.
    Resolverlo mediante un bucle for.
'''
def ejercicio08():

    b = int(2)

    for i in range(2, 29):
        co = int(0)
        if not(b % 2 == 0) or b == 2:
            for a in range(2, int(b/2)):
                if b % a == 0:
                    co += 1
                    a = b
            if co == 0:
                print(f'El cubo de {b} es {pow(b, 3)}')
        b += 1


'''
    9. Escribir un programa que lea la cantidad de empleados de una empresa y a continuación
    solicite el sueldo de cada empleado, visualizando a continuación cuál es el sueldo mayor.
'''
def ejercicio09():
    c = int(0)
    i = int(1)
    ce = int(0)
    
    smayor = float(0)
    sueldo = float(0)
    
    ce = int(input("Introduzca la cantidad de empleados: "))
    
    while i <= ce:
        sueldo = float(input(f'Introduzca el sueldo del empleado {i}: '))
        if sueldo > smayor:
            smayor = sueldo
            c = i
        i += 1
    print(f'El empleado con el sueldo mayor es el {c} con {smayor} €')
    



'''
    10. Escribir un programa que lea 5 números y escriba la media de los números leídos
    y los que están por encima de la media. 
'''
def ejercicio10():
    suma = int(0)
    media = int(0)
    c = int(0)
    
    temp = [int(input("Introduzca el primer numero: ")), 
            int(input("Introduzca el segundo numero: ")), 
            int(input("Introduzca el tercer numero: ")), 
            int(input("Introduzca el cuarto numero: ")), 
            int(input("Introduzca el quinto numero: "))]
    
    for i in range(len(temp)):
        suma += temp[i]

    media = suma / len(temp)
    
    for i in range(len(temp)):
        if temp[i] >= media:
            c += 1
            print(f'{temp[i]} es mayor o igual que la media')
    
    print(f'La media es {media} \nEl total de temperaturas >= media es {c}')
    
    
'''
    LLamada a los ejercicios
'''    
    
##ejercicio01()

##ejercicio02()

##ejercicio03()

##ejercicio04()

##ejercicio05()

##ejercicio06()

##ejercicio07()

##ejercicio08()

##ejercicio09()

##ejercicio10()