import random

def merge_sort(lista): # O(n log n)

    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        print(f'{lista}\n {izquierda} | {derecha}')

        # Llama recursiva por cada mitad hasta llegar a listas de 1 elemento
        merge_sort(izquierda)
        merge_sort(derecha)

        #Declaración de iteradores para las sublistas
        i = 0 #Sublista izquierda
        j = 0 #Sublista derecha

        #Iterador de la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):

            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
                k += 1
            else:
                lista[k] = derecha[j]
                j += 1
                k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'Izquierda {izquierda} | Derecha {derecha}\n{lista}Nice\n{"-" * 50}')
    
    return lista
    


if __name__ == '__main__':

    lista_tamaño = int(input('¿De qué tamaño será tu lista random?: '))
    lista_random = [random.randint(1, 100) for i in range(1, lista_tamaño)]

    lista = merge_sort(lista_random)
    print(f'\nTu lista antes de ordenar🤔\n{lista_random}')
    print(f'Tu lista ordenada😎\n{lista}')