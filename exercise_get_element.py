# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    if indice >= len(lista) or indice < (len(lista)*(-1)) :
        return None
    else:
        return lista[indice]
