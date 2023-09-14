print("Conversión de temperatura")

celsius = int(input("Ingrese los °C a convertir a °F: "))
fahrenheit = int(input("Ingrese los °F a convertir a °C: "))

eleccion = int(input("Elija qué conversión desea realizar: 1 - °C a °F. 2 - °F a °C. "))

def celsius_a_fahrenheit(celsius):
    pase1 = (celsius * 9 / 5) + 32
    return pase1

def fahrenheit_a_celsius(fahrenheit):
    pase2 = (fahrenheit - 32)* 5 / 9
    return pase2

if eleccion == 1:
    grado1 = celsius_a_fahrenheit(celsius)
    print ("Conversión: ", grado1, "°F")
elif eleccion == 2:
    grado2 = fahrenheit_a_celsius(fahrenheit)
    print("Conversión: ", grado2, "°C")
else:
    print ("La opción ingresada no es correcta.")

