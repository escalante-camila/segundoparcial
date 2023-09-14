print("Calculadora")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
operacion = int(input("Seleccione la operación a realizar: 1 - Suma, 2 - Resta, 3 - Multiplicación, 4- División."))

def suma(num1, num2):
    suma = num1 + num2
    return suma

def resta(num1, num2):
    resta = num1 - num2
    return resta

def multiplicacion(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion

def division(num1, num2):
    division = num1 / num2
    return division

if operacion == 1:
    resultado1 = suma(num1, num2)
    print("El resultado de la suma de los números ingresados es:", resultado1)
elif operacion == 2:
    resultado2 = resta(num1, num2)
    print("El resultado de la resta de los números ingresados es:", resultado2)
elif operacion == 3:
    resultado3 = multiplicacion(num1, num2)
    print("El resultado de la multiplicación de los números ingresados es:", resultado3)
elif operacion == 4:
    resultado4 = division(num1, num2)
    print("El resultado de la división de los números ingresados es:", resultado4)
else:
    print("La opción ingresada no es válida, intente nuevamente.")
