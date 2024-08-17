# Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo
# que numero = 10:
#           1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a
# un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
# while).
from re import search

def suma_repetitiva(numero) -> int: # se resuelve el punto 3aiii.
    suma = 0
    for i in range(1,numero+1): 
        suma += i
    return suma

def suma_triangular(numero) -> int: # bonus
    suma = numero*(numero+1)/2
    return int(suma)

def suma_recursiva(numero) -> int: # bonus
    if numero == 0: return numero
    return numero+suma_recursiva(numero-1)

def suma(numero) -> None:
    print("suma por repetición: ",suma_repetitiva(numero))
    print("suma por numero triangular: ",suma_triangular(numero))
    print("suma por recursividad: ",suma_recursiva(numero))

numero = input('Ingrese un número natural: ') # se resuelve el punto 3ai.
while (not search(r'^[0-9]+$', numero)): # se resuelve el punto 3aii.
    numero = input('Ingrese un número natural: ')

suma(int(numero))