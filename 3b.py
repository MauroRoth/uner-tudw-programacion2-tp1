# Escribir un programa que resuelva la secuencia de Fibonacci a pedido del
# usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro
# numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio
# anterior, validado. La función debe encargarse de calcular la secuencia para
# dicho número. Estas funciones permiten calcular el n-ésimo elemento de la sucesión
# de Fibonacci.

from math import sqrt, pow

def fibonacci_recursivo(numero):
    if numero<2:
        return numero
    return fibonacci_recursivo(numero-1)+fibonacci_recursivo(numero-2)

def fibonacci_repetitivo_1(numero):
    a = 0
    b = 1
    c = 0
    for i in range(numero):
        c = a + b
        a = b
        b = c
    return a

def fibonacci_repetitivo_2(numero):
    a = 0
    b = 1
    for i in range(numero):
        b = b + a
        a = b - a
    return a

def fibonacci_formula_explicita(numero):
    if numero<2:
        return numero
    else:
        phi = (1 + sqrt(5))/2 # número áureo
        j = (pow(phi,numero)-pow((1-phi),numero))/sqrt(5)
    return int(j)

def fibonacci_repetitivo_vector(numero):
    if numero<2:
        return numero
    else:
        vector = [x for x in range(numero+1)]
        vector[0] = 0
        vector[1] = 1
        for i in range(2,numero+1):
            vector[i] = vector[i-1]+vector[i-2]
        return vector[i]

def fibonacci_divideYvenceras(numero): # revisar porque no funciona
    if numero<2:
        return numero
    i = numero - 1
    auxOne = 0
    auxTwo = 1
    (a,b) = (auxTwo,auxOne)
    (c,d) = (auxOne,auxTwo)
    while i>0:
        if i%2!=0:
            auxOne = (d*b+c*a)
            auxTwo = (d*(b+a)+c*b)
            (a,b) = (auxOne,auxTwo)
        auxOne = int(pow(c,2)) + int(pow(d,2))
        auxTwo = d*(2*c+d)
        (c,d) = (auxOne,auxTwo)
        i = i/2
    return a+b
    
numero = int(input('Ingrese un número natural: '))
print("fibonacci recursivo: ",fibonacci_recursivo(numero))
print("fibonacci repetitivo 1: ",fibonacci_repetitivo_1(numero))
print("fibonacci repetitivo 2: ",fibonacci_repetitivo_2(numero))
print("fibonacci fórmula explícita: ",fibonacci_formula_explicita(numero))
print("fibonacci repetitivo vector: ",fibonacci_repetitivo_vector(numero))
#print("fibonacci divide y vencerás: ",fibonacci_divideYvenceras(numero))
