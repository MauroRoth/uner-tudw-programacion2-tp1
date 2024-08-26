# Tal como sucede con la lógica proposicional, en Python muchas veces las
# expresiones booleanas pueden ser simplificadas manteniendo el valor de
# verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
# a a and b. A continuación, intente simplificar las siguientes expresiones y
# escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
# valor de verdad de las expresiones ya simplificadas:
# i. (a or b) or (b and c)
# ii. b and c or False
# iii. a and b or c or (b and a)
# iv. a == True or b == False

def procesar_sentencias(a=False,b=False,c=False):
    sentencia0 = a and b # (a and b) or (b and a)
    sentencia1 = a or b # (a or b) or (b and c)
    sentencia2 = b and c # b and c or False
    sentencia3 = a and b or c # a and b or c or (b and a)
    sentencia4 = True # a == True or b == False
    print('a and b = ', sentencia0)
    print('a or b = ', sentencia1)
    print('b and c = ', sentencia2)
    print('a and b or c = ', sentencia3)
    print('True = ', sentencia4)

print('Reducción de expresiones lógicas: ')
print(50*'-')
a,b,c = False, True, False
print(f'a={a}, b={b}, c={c}')
print(50*'-')
procesar_sentencias(False,True,False)
