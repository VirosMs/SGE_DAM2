def max_product(numbers):
    """
        This function receives a list of numbers and returns the two numbers whose product is maximum among all the pairs.

        En Python, float('-inf') representa un número negativo infinito. Es un valor especial que se usa para representar 
        un número que es menor que cualquier otro número real.

        En el caso del código de max_product(), float('-inf') se usa para inicializar la variable max_product. 
        Esto asegura que el primer par de números que se compara será el par con el producto máximo encontrado hasta el momento.
    """

    max_product = float("-inf")
    max_numbers = ()
    for num1 in numbers:
        for num2 in numbers:
            if num1 != num2:
                product = num1 * num2
                if product > max_product:
                    max_product = product
                    max_numbers = (num1, num2)
    return max_numbers


numbers = [1, 2, 3, 4, 5]
max_numbers = max_product(numbers)
print(
    f"The two numbers whose product is maximum among all the pairs in {numbers} are {max_numbers}"
)
