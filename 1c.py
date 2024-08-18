# Escriba un procedimiento procesar_palabras(entrada) que acepte una
# secuencia de palabras separadas por coma, las ordene y las imprima.
# Suponiendo que la entrada provista al programa es la siguiente:
# te,felicito,que,bien,actuas
# La salida esperada es:
# actuas,bien,felicito,que,te

def procesa_palabras2(entrada):
    return ','.join(sorted(entrada.split(',')))

entrada = 'te,felicito,que,bien,actuas'
print(entrada)
print(procesa_palabras2(entrada))