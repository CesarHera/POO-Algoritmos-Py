import random
import time


def busqueda_binaria(objetivo, comienzo, final, lista):
    
    medio = (comienzo + final) // 2

    if comienzo > final:
        return False

    print(f'{objetivo}, Comienzo(index)={comienzo}, Final(index)={final} | Comienzo(valor)={lista[comienzo]}, Final(valor)={lista[final]}')

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(objetivo, medio + 1, final, lista)
    else:
        return busqueda_binaria(objetivo, comienzo, medio - 1, lista)



if __name__ == '__main__':
    
    objetivo = int(input('¿Cuál es el número a encontrar?: '))
    lista_tamaño = int(input('¿De qué tamaño será la lista (La lista se genera con números random desde 0 hasta el número que quieres encontrar)?: '))
    # lista = sorted([random.randint(0, objetivo) for i in range(lista_tamaño)])
    lista = range(lista_tamaño) #Hago esto para obtener el peor de los casos

    start = time.time()
    nice = busqueda_binaria(objetivo, 0, len(lista) - 1, lista)
    # print(lista)
    print(f'{objetivo} {"Está en la lista" if nice else "No está en la lista"}')
    end = time.time()
    print(end - start)