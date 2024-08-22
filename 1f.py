# Un portal web requiere un formulario de alta de usuario donde se ingrese,
# mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
# una función contrasena_valida(contrasena) que devuelva True en caso de
# superar las siguientes validaciones sobre la contraseña proporcionada por el
# usuario:
#     i. Longitud entre 6 y 20 caracteres.
#     ii. Debe contener al menos un número.
#     iii. Debe contener al menos dos mayúsculas.
#     iv. Debe contener al menos un carácter especial.
#     v. No puede contener espacios.
# La salida esperada es la siguiente:
#     abc.123 es válida:False
#     Abc.123 es válida:False
#     AbC.123 es válida:True
#     AbC.1 23 es válida:False
#     ÁbC.123 es válida:False
import re

def contrasena_valida(contrasena):
    regex1 = r'^.{6,20}$' # Longitud entre 6 y 20 caracteres.
    condicion1 = re.search(regex1,contrasena)
    regex2 = r'[0-9]+' # Debe contener al menos un número.
    condicion2 = re.search(regex2,contrasena)
    regex3 = r'[A-Z]+' #Debe contener al menos dos mayúsculas.
    condicion3 = len(re.findall(regex3,contrasena)) > 1
    regex4 = r'\W+' # Debe contener al menos un carácter especial.
    condicion4 = re.search(regex4,contrasena)
    regex5 = r'\s' # No puede contener espacios.
    condicion5 = re.search(regex5,contrasena)

    if condicion1 and condicion2 and condicion3 and condicion4 and not condicion5:
        return True
    return False

pruebas = [
    'abc.123', # es válida:False
    'Abc.123', # es válida:False
    'AbC.123', #  es válida:True
    'AbC.1 23',  # es válida:False
    'ÁbC.123', # es válida:False
]

for prueba in pruebas:
    print(contrasena_valida(prueba))
