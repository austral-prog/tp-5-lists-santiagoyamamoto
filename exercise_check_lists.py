# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    if len(lista1) < 4 or len(lista2) < 4:
        return False
    elif lista1[2] == lista2[2]:
        return True
    else:
        return False
