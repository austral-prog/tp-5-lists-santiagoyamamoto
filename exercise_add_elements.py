# Ejercicio 3: Agregar elementos al principio y final
from mistune.plugins.formatting import insert


def add_elements(lista):
    lista.insert(0,'Pink')
    lista.append('Yellow')
    return lista

