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
    lista = list(set(lista))
    lista.sort(reverse = True)
    lista2 = []
    for elemento in lista:
        if elemento % 2 == 0:
            lista2.append(elemento)
    suma = sum(lista2)
    lista2.insert(0, suma)
    return lista2
    
lista = [2, 4, 5, 65, 83, 23]
nueva_lista = modificar(lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))
