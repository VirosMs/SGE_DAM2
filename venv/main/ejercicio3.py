def ejercicio01():
    n1 = float(input("Ingrese la nota del primero aluno: "))
    n2 = float(input("Ingrese la nota del segundo aluno: "))
    n3 = float(input("Ingrese la nota del tercero aluno: "))

    p = (n1 + n2 + n3) / 3

    print(round(p, 2))


def ejercicio02():
    base = float(input("Ingrese la BASE del rectángulo: "))
    alto = float(input("Ingrese el ALTO del rectángulo: "))

    sup = base * alto

    per = 2 * (base + alto)

    print(f'La superfice del rectángulo es: {sup}')
    print(f'El perímetro del rectángulo es: {per}')


def ejercicio03():
    x = int(input("Ingrese el primero numero: "))
    y = int(input("Ingrese el segundo numero: "))

    if x > y:
        print(f'El menor es el segundo numero, con el valor: {y}')
    else:
        print(f'El menor es el primero numero, con el valor: {x}')


def ejercicio04():
    anio = int(input("Ingrese el año: "))

    if (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0):
        print("El año es BISIESTO")
    else:
        print("El año NO es BISIESTO")


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



##ejercicio01()

##ejercicio02()

##ejercicio03()

##ejercicio04()

##ejercicio05()

##ejercicio06()

##ejercicio07()

ejercicio08()
