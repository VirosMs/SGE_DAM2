
from datetime import datetime

class Persona:
    def __init__(self, nombre , id, telefono, email, direccion):
        self.nombre = nombre
        self.id = id
        self.__telefono = telefono
        self.email = email
        self.direccion = direccion
    
    @staticmethod
    def get_telefono(persona):
        return persona.__telefono
        
    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Email: {self.email}, Dirección: {self.direccion}"
    
    def get_telefono(self):
        return self.__telefono
    
class Cliente(Persona):
    def __init__(self, nombre, id, telefono, email, direccion):
        super().__init__(nombre, id, telefono, email, direccion)
        self.ultima_compra = ([], None)
        
    def compra(self, *args):
        self.ultima_compra = (args, datetime.now())

class Empleado(Cliente, Persona):
    numeroEmpleados = 0
    
    def __init__(self, nombre, id, telefono, email, direccion, seccion, supervisor, numeroCuenta):
        super().__init__(nombre, id, telefono, email, direccion)
        self.__numero_cuenta = numeroCuenta
        self.seccion = seccion
        self.supervisor = supervisor
        Empleado.numeroEmpleados += 1
        
    def __str__(self):
        return f"{super().__str__()}, Sección: {self.seccion}, Supervisor: {self.supervisor}"
    
    @staticmethod
    def get_numero_cuenta(empleado):
        return empleado.__numero_cuenta
    
    @classmethod
    def mostrar_numero_empleados(cls):
        print(f"El número de empleados es: {cls.numeroEmpleados}")
        
    @classmethod
    def reducir_numero_empleados(cls):
        cls.numeroEmpleados -= 1
        

    @classmethod
    def aumentar_numero_empleados(cls):
        cls.numeroEmpleados += 1



# Crear una instancia de la clase Persona
persona1 = Persona("Charles", "123456", "999-9999", "charles@gmail.com", "Calle 123")

# Acceder a los atributos de la instancia de Persona
print(persona1.nombre)
print(persona1.id)
print(persona1.email)
print(persona1.direccion)

# Crear una instancia de la clase Cliente
cliente1 = Cliente("Ana", "654321", "444-4444", "ana@gmail.com", "Calle 456")

# Acceder a los atributos de la instancia de Cliente
print(cliente1.nombre)
print(cliente1.id)
print(cliente1.email)
print(cliente1.direccion)

# Realizar una compra con la instancia de Cliente
cliente1.compra("producto1", "producto2", "producto3")

# Acceder a la última compra realizada por la instancia de Cliente
print(cliente1.ultima_compra)

# Crear una instancia de la clase Empleado
empleado1 = Empleado("Pedro", "987654", "333-3333", "pedro@gmail.com", "Calle 789", "Sección 1", "Supervisor 1", "0000-0000-0000")

# Acceder a los atributos de la instancia de Empleado
print(empleado1.nombre)
print(empleado1.id)
print(empleado1.email)
print(empleado1.direccion)
print(empleado1.seccion)
print(empleado1.supervisor)

# Acceder al número de cuenta de la instancia de Empleado utilizando el método estático
print(Empleado.get_numero_cuenta(empleado1))

# Acceder al número de teléfono de la instancia de Empleado utilizando el método de instancia
print(Empleado.get_telefono(empleado1))

# Mostrar el número de empleados utilizando el método de clase
Empleado.mostrar_numero_empleados()

# Aumentar el número de empleados utilizando el método de clase
Empleado.aumentar_numero_empleados()

# Mostrar el número de empleados utilizando el método de clase
Empleado.mostrar_numero_empleados()

# Reducir el número de empleados utilizando el método de clase
Empleado.reducir_numero_empleados()

# Mostrar el número de empleados utilizando el método de clase
Empleado.mostrar_numero_empleados()



