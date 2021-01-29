import random

def busqueda_binaria(objetivo, comienzo, final, lista):
    print(f'{objetivo}, {lista[comienzo]}, {lista[final]}')
    if comienzo == final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(objetivo, medio + 1, final, lista)
    else:
        return busqueda_binaria(objetivo, comienzo, medio - 1, lista)


if __name__ == '__main__':
    objetivo = int(input('¿Cuál es el número a encontrar?: '))
    lista_tamaño = int(input('¿De qué tamaño será la lista?: '))
    lista = sorted([random.randint(0, 100) for i in range(lista_tamaño)])

    nice = busqueda_binaria(objetivo, 0, len(lista) - 1, lista)

    print(lista)
    print(f'{objetivo} {"Está en la lista" if nice else "No está en la lista"}')