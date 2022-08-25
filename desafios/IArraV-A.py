from math import ceil
from random import randint
#################
## ADVERTENCIA 
## Este código escala su tiempo de computo con el valor de los números
## si sumas números muy grandes la respuesta puede tardar muchísimo
## no se recomienda sumar números mayores a 1e7
## usese bajo el propio riesgo

def sumar():
    print("Ingresa los números que quieres sumar")    
    numero_a = float(input())
    numero_b = float(input())

    if numero_a < 0 or numero_b < 0:
        return numero_a + numero_b

    diferencia_a = ceil(numero_a) - numero_a
    diferencia_b = ceil(numero_b) - numero_b
    lista_a = []
    lista_b = []
    
    for unidad in range(int(ceil(numero_a))):
        lista_a.append("1")

    for unidad in range(int(ceil(numero_b))):
        lista_b.append("1")

    suma_a = 0
    suma_b = 0

    for unidad in lista_a:
        suma_a += int(unidad)

    for unidad in lista_b:
        suma_b += int(unidad)

    suma = 0

    for unidad in range(suma_a + suma_b):
        suma += 1

    diferencias = diferencia_a + diferencia_b
    decision_de_Diosito = False
    lista_de_chances = list(range(suma + 1))

    var = randint(lista_de_chances[0],lista_de_chances[-1])

    while not decision_de_Diosito:

        if randint(lista_de_chances[0],lista_de_chances[-1]) == suma:
            respuesta = suma - diferencias
            decision_de_Diosito = True

    return respuesta

suma = sumar()
print(suma)
