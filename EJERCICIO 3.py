print ("Búsqueda")
num = input("Ingrese el número que desea encontrar en el arreglo: ")
arreglo = []
continuar = 1

while continuar == 1:
    numero = int(input("Ingrese un número para el arreglo: "))
    arreglo.append(numero)
    continuar = int(input("Si desea seguir agregando números seleccione <1>: "))


def busqueda(arreglo, num):
    num_encontrado = False
    for elemento in arreglo:
        if elemento == num:
            print("El elemento", num, "se encuentra en el arreglo.")
            elemento_encontrado = True
            break

    return ("El número se encuentra en el arreglo.")

if continuar != 1:
    encontro = busqueda(arreglo, num)
    print ("Se encontró el número?:", encontro)