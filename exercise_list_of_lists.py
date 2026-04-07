# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    
    lista1 = lista_de_listas[:][0]
    lista2 = lista_de_listas[:][1]
    lista3 = lista_de_listas[:][2]

    if len(lista1) == 0:
        lista11= []
    elif len(lista1) == 1:
        lista11 = lista1[:]
    else:
        lista11= lista1[:][0:2]

    if len(lista2) == 0 or len(lista2) == 1:
        lista22 = []
    elif len(lista2) == 2:
        lista22 = lista2[:][1]
    elif len(lista2) == 3:
        lista22 = lista2[:][1:3]
    else:
        lista22 = lista2[:][1:4]

    if len(lista3) == 0:
        lista33 = []
    elif len(lista3) == 1:
        lista33 = lista3[:]
    else:
        lista33 = lista3[:][-2:]

    total = [lista11, lista22, lista33]
    return total
