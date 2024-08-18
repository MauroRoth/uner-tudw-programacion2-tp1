# Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y
# cuando las letras que componen dicha palabra estén en orden alfabético, y False
# en caso contrario.

def es_abc(palabra):
    if list(palabra) == sorted(palabra):
        return True
    return False

palabra = 'alícuota'
print(es_abc(palabra))