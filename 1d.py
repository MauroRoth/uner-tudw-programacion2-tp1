# Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
# que tome ambas como parámetros e imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

def listas_diferencia(lista1,lista2):
    elementos_comunes = list()
    elementos_no_comunes = list()
    for elemento in lista1:
        if elemento in lista2:
            elementos_comunes.append(elemento)
    for elemento in (lista1+lista2):
        if elemento not in elementos_comunes:
            elementos_no_comunes.append(elemento)
    return sorted(elementos_comunes,reverse=True),sorted(elementos_no_comunes)

lista1 = ['b', 'a', 'c']
lista2 = ['e', 'b', 'd', 'c']
print(listas_diferencia(lista1,lista2)[0])
print(listas_diferencia(lista1,lista2)[1])
