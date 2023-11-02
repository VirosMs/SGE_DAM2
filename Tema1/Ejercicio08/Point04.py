cosa = input("Please enter something: ")
try:
    r = 34/float(cosa)
except Exception as e:
    print("Se ha producido una excepción:", type(e).__name__, e)
    r = 0

fichero = None
try:
    calabaza = "example.txt"
    fichero = open(calabaza)
    mi_lista = []

    for i in range(20):
        mi_lista.append(input(f"Enter number {i+1}: "))
    patata = mi_lista[15] + ' Enter number:'

    print(fichero.read())
except (FileNotFoundError, FileExistsError) as e:
    print("Se ha producido una excepción:", type(e).__name__, e)
finally:
    if fichero is not None:
        fichero.close()
