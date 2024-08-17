import time
from re import search
from funciones import * # aquí se realizó el punto 2e.

# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
while (not search(r'^[0-9]+$',edad)): # aquí se realizó el punto 2c
    edad = input("Ingrese su edad: ")
     
# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = edad_en_dias(hora_local,anio_comienzo,anio_fin)

# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))
