import random


def bubble_sort(lista):

    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(**2) Algorítmo cuadrático
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]                
    
    return lista



if __name__ == '__main__':
    lista_tamaño = int(input('¿De qué tamaño será tu lista random?: '))
    
    lista = [random.randint(1, 100) for i in range(lista_tamaño)]
    print(lista)

    lista = bubble_sort(lista)
    print(f'\n {lista}') #\n es un salto de renglón para separar las listas