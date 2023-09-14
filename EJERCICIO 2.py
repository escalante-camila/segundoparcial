print("Números primos en un rango")

numeros = []
continuar = 1

while continuar == 1:
    numero = int(input("Ingrese un número para el arreglo: "))
    numeros.append(numero)
    continuar = int(input("Si desea seguir agregando números seleccione <1>: "))


def numero_primo(num):
    primo = False
    if num >= 1 and num <= 3:
        primo = True
    elif num % 2 != 0 or num % 3 != 0:
        primo = True
    return primo

def suma_numeros_primos(numeros):
    suma_primos = 0
    num_primos = 0
    for numero in numeros:
        if numero_primo(numero):
            suma_primos += numero
            num_primos += 1
    return ("El resultado de la suma de los números primos del arreglo ingresado es: ", suma_primos)

realizar = int(input("Ingrese 1 si quiere realizar la suma de los números primos del rango ingresado: "))

if realizar == 1:
    suma = suma_numeros_primos(numeros)
    print ("Resultado: ", suma)
