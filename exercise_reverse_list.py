# Ejercicio 8: Invertir una lista

def reverse_list(lista):
    if len(lista) == 0:
        return []
    else:
        return lista[:][::-1]
