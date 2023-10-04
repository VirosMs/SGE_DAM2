#Charles Arruda Santos

#“Los ejercicios están separados por los comentarios de sus respectivos enunciados”
#“Para asegurar que mis métodos se ejecuten correctamente, los invoco al final del archivo”

# 1. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

def ejercicio01():
    name = input("User name: ")
    print("¡Hola " + name + " !")


# 2. Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:


def ejercicio02():
    num = int(input("Escribe un numero positivo: "))

    total = 0

    if num > 0:
        for count in range(num):
            total = num * (num + 1) / 2
        print("La suma de los n primeros enteros positivos son " + str(total))
    else:
        print(
            "El numero '" + str(num) + "' es negativo, hay que ser un numero positivo"
        )


# 3. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


def ejercicio03():
    initialMoney = float(input("Cantidad de dinero depositada: "))

    interesAnual = 1.04

    balanceAfterYear = float(initialMoney * interesAnual)

    balanceAfterTwoYears = float(balanceAfterYear * interesAnual)

    balanceAfterTreeYears = float(balanceAfterTwoYears * interesAnual)

    print(f"Saldo después del primer año: {round(balanceAfterYear, 2)}")
    print(f"Saldo después del segundo año: {round(balanceAfterTwoYears, 2)}")
    print(f"Saldo después del tercer año: {round(balanceAfterTreeYears, 2)}")


# 4. Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. Hazlo de dos formas distintas, utilizando un bucle y sin utilizarlo.


def ejercicio04():
    name = input("Cual es tu nombre? ")
    num = int(input("Escribe un numero positivo: "))

    if num > 0:
        # doing without bucle
        for x in range(num):
            print(f"{x + 1}: {name.upper()}")

        print("-------------------------")
        # Doing without bucle
        print("\n".join([name.upper()] * num))


# 5. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


def ejercicio05():
    name = input("Cual es tu nombre? ")

    print(f"{name.upper()} tiene {len(name)}")


# 6. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


def ejercicio06():
    bNum = input("Ingrese un número de teléfono con formato +34-XXXXXXXXX-XX: ")

    partes = bNum.split("-")

    if (
        len(partes) == 3
        and partes[0] == "+34"
        and len(partes[1]) == 9
        and len(partes[2]) == 2
    ):
        print(f"Número de teléfono sin prefijo ni extensión: {partes[1]}")
    else:
        print("El número de teléfono no tiene el formato correcto.")


#7. Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minúscula, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula. Por ejemplo:
#Aprende a programar con Python
#a
#Aprende A progrAmAr con Python

def ejercicio07():
    phrase = input("Escribe un frase: ")
    vowel = input("Introduzca una vocal en minuscula: ").lower()
    answer = ""

    if len(vowel) == 1:
        answer = phrase.replace(vowel, vowel.upper())
        print(answer)
    else:
        print("Solo puedes introduzir una vocal")


# 8. Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
# 125.72
# 125 euros y 72 céntimos.


def ejercicio08():
    money = input("Escribe el precio de productos con decimales separados por '.' : ")

    parts = money.split(".")

    if len(parts) == 2:
        print(parts[0] + " euros y " + parts[1] + " céntimos.")
    else:
        print("Tienes que poner los centimos")


# 9. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def ejercicio09():
    passN = input("Escribe tu contraseña : ")

    passW = "HelloWorld"

    if passN.casefold() == passW.casefold():
        print("Las contraseñas son iguales")
    else:
        print("Las contrasñas no son iguales")



#10. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def ejercicio10():
    age = int(input("Escribe tu edad: "))
    income = float(input("Escribe tus ingresos mensuales: "))
    
    if age > 16 and income > 1000:
        print("Tienes que tributar D:")
    else:
        print("No tienes que tributar :D")
        

#11. Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	                Tipo impositivo
#Menos de 10000€	        5%
#Entre 10000€ y 20000€	    15%
#Entre 20000€ y 35000€	    20%
#Entre 35000€ y 60000€	    30%
#Más de 60000€	            45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def ejercicio11():
    annualRent = float(input("Escribe tu renta anual: "))
    
    rentType = 5
        
    if annualRent > 10000:
        if annualRent > 20000:
            if annualRent > 35000:
                if annualRent > 60000:
                    rentType = 45
                else:
                    rentType = 30
            else:
                rentType = 20
        else: 
            rentType = 15

    print(f"El tipo de impuesto que te corresponde es el {rentType}%")
    

#12. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def ejercicio12():    
    allPizza = ['Mozzarella', 'Tomate']
    vegan = ['Pimiento', 'tofu']
    noVegan = ['Peperoni', 'Jamón', 'Salmón']
    answer = 0
    
    #Pregunto si quiere un plato vegano o no 
    sw = input("Quieres un plato vegano? si/no: ")
    
    #Pregunto que ingredientes quiere
    if sw.casefold() == "si":
        print(f"MENU Vegano\n1.{vegan[0]}\n2.{vegan[1]}\n")
        answer = int(input("Ingrediente: "))-1
    elif sw.casefold() == "no":
        print(f"MENU NO Vegano\n1.{noVegan[0]}\n2.{noVegan[1]}\n3.{noVegan[2]}\n")
        answer = int(input("Ingrediente: "))-1
    else:
        print("Respuesta no valida")
    
    #Imprimo la respuesta
    print(f"\nElegio una pizza vegana? {sw}")
    if sw.casefold() == "si":
        print(f"Los ingredientes fueron: {vegan[answer]}, {allPizza[0]}, {allPizza[1]}")
    elif sw.casefold() == "no":
        print(f"Los ingredientes fueron: {noVegan[answer]}, {allPizza[0]}, {allPizza[1]}")
    else:
        print("Error")


#13. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.b 

def ejercicio13():
    valueInitial = float(input("Cuanto quieres investir? "))
    years = int(input("Cuantos años queires investir? "))
    annualInterest = float(input("Cual es el interes anual? "))
    
    for year in range(1, years + 1):
        accumulatedCapital = valueInitial * (1 + (annualInterest / 100))
        print(f"Después de {year} años, tendrás un capital de {round(accumulatedCapital, 2)}")
        valueInitial = accumulatedCapital


#14. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def ejercicio14():
    passW = "HolaMundo"
    
    passN = input("Escribe la contraseña: ")
    
    while passW != passN:
        print("Contraseña esta mal. ")
        passN = input("Escribe la contraseña novamente: ")
    
    print("Contraseña correcta :P")


#15. Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def ejercicio15():
    phrase = input("Escribe una frase: ")
    letter = input("Escribe una letra: ")
    
    numLetter = phrase.count(letter)
    
    print(f"La letra {letter} aparece {numLetter} en la frase")



#16. Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
#Es el mismo que el 15




#17. Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def ejercicio17():
    sw = True
    
    while sw:
        value = input("Escribe algo (o 'salir' para terminar): ")
        if value.casefold() == "salir":
            sw = False  # Termina el bucle si el usuario escribe "salir"
        else:
            print(value)


#18. Escribir una función que invierta una cadena de texto. Utilizala para invertir una frase pedida al usuario y luego mostrarla por pantalla.

def ejercicio18():
    text = input("Escribe un acadena de texto: ")
        
    print(f"{text[::-1]}")


#19. Escribir una función llamada expo que dados dos números, base y exponente, devuelve el resultado de elevar la base al exponente. Crea un programa que pida dos números al usuario y muestre el resultado. Comprueba que los números son enteros y positivos. De no serlo avisa al usuario mediante un mensaje.

def expo(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

def ejercicio19():
    while True:
        try:
            base = int(input("Ingrese un número base entero positivo: "))
            exponente = int(input("Ingrese un número exponente entero positivo: "))
            
            if base < 0 or exponente < 0:
                print("Ambos números deben ser enteros y positivos. Inténtelo nuevamente.")
            else:
                resultado = expo(base, exponente)
                print(f"{base} elevado a la {exponente} es igual a {resultado}")
                break
        except ValueError:
            print("Debe ingresar números enteros válidos. Inténtelo nuevamente.")




#20. Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.


# Función para aplicar un descuento a un precio
def applyDiscount(price, discount):
    return price - (price * discount / 100)

# Función para aplicar el IVA a un precio
def applyIva(price, iva):
    return price + (price * iva / 100)

# Función para calcular el precio final de una cesta de compra
def calcFinalPrice(cesta, funcion):
    finalPrice = 0
    for producto, price in cesta.items():
        finalPrice += funcion(price, cesta[producto])
    return finalPrice

# Función principal que solicita la cesta de compra y la operación a realizar
def ejercicio20():
    shoppingCart = {
        'Producto1': 100,
        'Producto2': 50,
        'Producto3': 75
    }

    operacion = input("Elija la operación a realizar (descuento/iva): ").lower()

    if operacion == "descuento":
        discount = float(input("Introduzca el porcentaje de descuento: "))
        finalPrice = calcFinalPrice(shoppingCart, lambda price, i: applyDiscount(price, discount))
        print(f"Precio final con descuento del {discount}%: {finalPrice}")
    elif operacion == "iva":
        iva = float(input("Introduzca el porcentaje de IVA: "))
        finalPrice = calcFinalPrice(shoppingCart, lambda price, i: applyIva(price, iva))
        print(f"Precio final con IVA del {iva}%: {finalPrice}")
    else:
        print("Operación no válida. Por favor, elija 'descuento' o 'iva'.")



#Invocando los metodos

#ejercicio01()
#ejercicio02()
#ejercicio03()
#ejercicio04()
#ejercicio05()
#ejercicio06()
#ejercicio07()
#ejercicio08()
#ejercicio09()
#ejercicio10()
#ejercicio11()
#ejercicio12()
#ejercicio13()
#ejercicio14()
#ejercicio15()
#ejercicio17()
#ejercicio18()
#ejercicio19()
ejercicio20()
