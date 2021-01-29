import random
import time


def busqueda_lineal(objetivo, lista): # Complejidad algorítmica: O(n)
    
    contador = 0

    for i in lista:
        contador += 1
        if i == objetivo:
            return [contador, True]
    
    return [contador, False]



if __name__ == '__main__':

    objetivo = int(input('¿Ingresa el número que quieres encontrar?: '))
    lista_tamaño = int(input('¿De qué tamaño genero la lista aleatoria?: '))
    # lista = [random.randint(1, objetivo) for i in range(lista_tamaño)]
    lista = range(lista_tamaño) #Hago esto para obtener el peor de los casos

    start = time.time()
    contador, nice = busqueda_lineal(objetivo, lista)

    # print(lista)
    print(f'{objetivo} {"está en la lista" if nice else "no está en la lista"}')
    end = time.time()
    print((end - start))
    print(contador)