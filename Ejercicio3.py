#Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#Borrar los elementos duplicados.
# Ordenar la lista de mayor a menor.
# Eliminar todos los números impares.
# Realizar una suma de todos los números que quedan.
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
# nueva_lista = modificar(lista)
# print( nueva_lista[0] == sum(nueva_lista[1:]) )
# True

def modificar(lista):
    lista = sorted(lista, reverse = True)