"""
3. Implementa en Python un programa que resuelva el siguiente problema:
Vamos a llevar la lista de pedidos de un restaurante italiano en Python. La carta va a estar limitada a una serie de platos, 
fundamentalmente combinaciones de ingredientes sencillos.
Pasta: espaguetis, macarrones y fusili.
Salsas: carbonara, rabiosa, pesto verde, pesto rojo, boloñesa.
Pizza: clásica, integral.
Ingredientes para pizzas: extra de queso, queso azul, salchicha, carne, chorizo, jamón, pimiento verde, aceitunas, anchoas, atún, salmón, piña.
Tiramisu, panna cotta.
La pasta tendrá una única salsa, la pizza puede tener hasta 5 ingredientes.
Cada mesa/usuario realizará su pedido, que se guardará en una lista que se le mostrará junto con el precio total.

"""

def carta():
    carta = {
        "Pasta": {"Espaguetis": 5, "Macarrones": 4, "Fusili": 4.5},
        "Pizza": {"Clásica": 8, "Integral": 9}
    }
    Salsas: {"Carbonara": 2, 
                "Rabiosa": 2.5, 
                "Pesto verde": 2.5, 
                "Pesto rojo": 2.5, 
                "Boloñesa": 2}
    
    ingredientePizza = {
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
    
    postre = {
        "Tiramisu": 6,
        "Panna cotta": 5.5
    }

    precio = (int)
    
    
    if input(f'Quieres pasta? si/no').casefold("si"):
        sals = input(f'Elige una salsa: ')
        if sals in carta["Pasta"][sals]:
            precio = carta["Pasta"][sals]
        else:
            print(f'Hay que eligir una salsa validad.')    
            
    if input(f'Quieres Pizza? si/no').casefold("si"):
        print(precio)
    
