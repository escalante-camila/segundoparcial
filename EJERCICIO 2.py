numeros = []
continuar = 1

while continuar == 1:
    numero = int(input("Ingrese un número para el arreglo: "))
    numeros.append(numero)
    continuar = int(input("Si desea seguir agregando números seleccione <1>: "))

def numero_primo(num):
    primo = False
    num_primos = []
    for num in numeros:
        if num == 2 or num == 3:
            num_primos.append(num)
            primo = True
        elif num == 1:
            primo = False
        elif num % 2 != 0 or num % 3 != 0:
            num_primos.append(num)
            primo = True
        else: 
            print("No es primo.")
    return num_primos

realizar = int(input("Ingrese 1 ver los números primos del arreglo: "))

if realizar == 1:
    mostrar = numero_primo(numeros)
    print (mostrar)
else: 
    print("Fin del programa.")
