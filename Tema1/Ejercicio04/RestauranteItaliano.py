
# Function to show the menu of the restaurant and return the menu as a dictionary
def mostrar_carta():
    carta = {
        "Pasta": {"Espaguetis": 5, "Macarrones": 4, "Fusili": 4.5},
        "Pizza": {"Clásica": 8, "Integral": 9}
    }
    salsas = {
        "Carbonara": 2,
        "Rabiosa": 2.5,
        "Pesto verde": 2.5,
        "Pesto rojo": 2.5,
        "Boloñesa": 2
    }

    ingredientes_pizza = {
        "Extra de queso": 1,
        "Queso azul": 2,
        "Salchicha": 1.5,
        "Carne": 2,
        "Chorizo": 2.5,
        "Jamón": 3,
        "Pimiento verde": 1,
        "Aceitunas": 1.5,
        "Anchoas": 3,
        "Atún": 2.5,
        "Salmón": 3,
        "Piña": 1.5
    }

    postres = {
        "Tiramisu": 6,
        "Panna cotta": 5.5
    }

    print("**Carta de restaurante italiano**")
    print("**Pasta**")
    for tipo_pasta, precio in carta["Pasta"].items():
        print(f"{tipo_pasta:10}: {precio:.2f}")
    print("**Salsas**")
    for salsa, precio in salsas.items():
        print(f"{salsa:10}: {precio:.2f}")
    print("**Pizza**")
    for tipo_pizza, precio in carta["Pizza"].items():
        print(f"{tipo_pizza:10}: {precio:.2f}")
    print("**Ingredientes para pizzas**")
    for ingrediente, precio in ingredientes_pizza.items():
        print(f"{ingrediente:10}: {precio:.2f}")
    print("**Postres**")
    for tipo_postre, precio in postres.items():
        print(f"{tipo_postre:10}: {precio:.2f}")
    print("")

    return carta, salsas, ingredientes_pizza, postres


# Function to calculate the total price of the order and return it as a float
def calcular_precio_pedido(carta, salsas, ingredientes_pizza, postres):
    precio_total = 0
    sw = True
    if input('¿Quieres pasta? si/no: ').casefold() == "si":
        while sw:        
            tipo_pasta = input('Elige el tipo de pasta: ')
            if tipo_pasta in carta["Pasta"]:
                precio_total += carta["Pasta"][tipo_pasta]
                salsa = input('Elige una salsa: ')
                if salsa in salsas:
                    precio_total += salsas[salsa]
                    sw = False
                else:
                    print('Debes elegir una salsa válida.')
            else:
                print('Debes elegir un tipo de pasta válida.')

    sw = True
    if input('¿Quieres pizza? si/no: ').casefold() == "si":
        while sw: 
            tipo_pizza = input('Elige el tipo de pizza: ')
            if tipo_pizza in carta["Pizza"]:
                precio_total += carta["Pizza"][tipo_pizza]

                ingredientes = []
                for i in range(1, 6):
                    ingrediente = input(f'Ingrediente {i}: ')
                    if ingrediente in ingredientes_pizza:
                        ingredientes.append(ingrediente)
                        sw = False
                    else:
                        print('Debes elegir un ingrediente válido.')
                        sw = True

                for ingrediente in ingredientes:
                    precio_total += ingredientes_pizza[ingrediente]
                
            else:
                print('Debes elegir un tipo de pizza válido.')

    sw = True
    if input('¿Quieres postre? si/no: ').casefold() == "si":
        while sw:
            tipo_postre = input('Elige el postre: ')
            if tipo_postre in postres:
                precio_total += postres[tipo_postre]
                sw = False
            else:
                print('Debes elegir un postre válido.')

    return precio_total

# Main program function to call the other functions
def main():
    carta, salsas, ingredientes_pizza, postres = mostrar_carta()
    precio_total = calcular_precio_pedido(carta, salsas, ingredientes_pizza, postres)
    print(f"El precio total es: {precio_total:.2f}")


# Main program
if __name__ == "__main__":
    main()

"""
_summary_
    This program shows the menu of an Italian restaurant and calculates the total price of the order.
_end_summary_
"""