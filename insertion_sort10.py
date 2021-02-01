import random

def insertion_sort(lista):
    
    for indice in range(1, len(lista)): #O(n**2) Algorítmo cuadrático

        posicion_actual = indice
        valor_actual = lista[indice]

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:

            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        
        lista[posicion_actual] = valor_actual
    
    return lista



if __name__ == '__main__':

    lista = insertion_sort([random.randint(1, 100) for i in range(1, 10)])
    print(lista)