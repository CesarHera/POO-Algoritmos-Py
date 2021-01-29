import random

def busqueda_lineal(objetivo, lista): # Complejidad algorítmica: O(n)
    
    for i in lista:
        if i == objetivo:
            return True
    
    return False


if __name__ == '__main__':
    objetivo = int(input('¿Ingresa el número que quieres encontrar?: '))
    lista_tamaño = int(input('¿De qué tamaño genero la lista aleatoria?: '))

    lista = sorted([random.randint(1, 100) for i in range(lista_tamaño)])

    nice = busqueda_lineal(objetivo, lista)

    print(lista)
    print(f'{objetivo} {"está en la lista" if nice else "no está en la lista"}')