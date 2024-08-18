# Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de
# números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista
# e imprima ambas. La lista de números la ingresa el usuario en forma de números
# separados por coma.
# Suponiendo que el usuario ingresa la siguiente lista:
# 1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81

def numero_par_impar(entrada):
    par = list(filter(lambda x: x%2==0, entrada))
    impar = list(map(lambda x: x**2,filter(lambda x: x%2!=0, entrada)))
    return par,impar

entrada = ((input('Ingrese lista de números separados por coma: ')).split(','))
entrada = list(map(lambda x:int(x),entrada))

print(entrada)
print(numero_par_impar(entrada)[0])
print(numero_par_impar(entrada)[1])
