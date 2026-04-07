# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    if len(lista) == 1 or len(lista) == 2 or len(lista) == 3 or len(lista) == 4:
        del lista[0]
    elif len(lista) == 5:
        del lista[4]
        del lista[0]
    elif len(lista) == 0:
        ""
    else:
        del lista[0]
        del lista[3:5]
    return lista
