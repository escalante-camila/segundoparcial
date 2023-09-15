numeros = []
continuar = 1

while continuar == 1:
    numero = int(input("Ingrese un número para el arreglo: "))
    numeros.append(numero)
    continuar = int(input("Si desea seguir agregando números seleccione <1>: "))


def numero_primo(numeros):
    primos = []
    for num in numeros:
        if num <= 1:
            primo = False
        elif num == 2 or num == 3:
            primo = True
            primos.append(num)
        elif num % 2 != 0 and num % 3 != 0:
            primo = True
            primos.append(num)
        else: 
            primo = False
    return primos

realizar = int(input("Ingrese 1 ver los números primos del arreglo: "))

if realizar == 1:
    mostrar = numero_primo(numeros)
    print(mostrar)
else: 
    print("Fin del programa.")
