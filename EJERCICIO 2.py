print("Números primos en un rango")


rango = []
continuar = 1

while continuar == 1:
    numero = int(input("Ingrese un número para el arreglo: "))
    rango.append(numero)
    continuar = int(input("Si desea seguir agregando números seleccione <1>: "))


def numero_primo(num):
    primo = False
    if num >= 1 and num <= 3:
        primo = True
    elif num2 % 2 != 0 or num % 3 != 0:
        primo = True
    return primo

def suma_numeros_primos(rango):
    suma_primos = 0
    num_primos = 0
    for rang in rango:
        if num_primos(rango[rang]):
            suma_numeros_primos += rang
            num_primos += 1
    return ("El resultado de la suma de los números primos del arreglo ingresado es: ", suma_numeros_primos)

realizar = int(input("Ingrese 1 si quiere realizar la suma de los números primos del rango ingresado: "))

if realizar == 1:
    suma = suma_numeros_primos(rango)
    print ("Resultado: ", suma)