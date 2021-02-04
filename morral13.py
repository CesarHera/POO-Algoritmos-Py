def morral(espacio_morral, pesos, valores, n, mensaje):
    print('-' * 50)
    print(mensaje)
    print(f'   * Analizamos Elemento {n} *')
    print(f'   - Espacio en morral = {espacio_morral}')
    print(f'   - Peso = {pesos[n - 1]}, valor = {valores[n - 1]} ')

    if n == 0 or espacio_morral == 0:
        #Puse este print para enterarme de cuándo se entra en este if
        if espacio_morral == 0:
            print('   Espacio en morral lleno!')
        elif n == 0:
            print('   Indice final alcanzado!') 
        return 0
    
    if pesos[n - 1] > espacio_morral:
        #Este print también es para saber cuando se entra a este if
        print('     peso del elemento > espacio del morral')
        return morral(espacio_morral, pesos, valores, n - 1, '')
    
    #Este print tan solo imprime ambos resultados posibles del max() y también impríme cuál fue el más grande para saber cuál eligió.
    return max(valores[n - 1] + morral(espacio_morral - pesos[n - 1], pesos, valores, n - 1, f'--> SI Robo el elemento {n} y sumo a mi morral {valores[n - 1]} en valor!'), 
                morral(espacio_morral, pesos, valores, n - 1, f'--> NO robo el elemento {n}!'))


if __name__ == '__main__':
    espacio_morral = 50
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    n = len(valores)

    resultado = morral(espacio_morral, pesos, valores, n, 'Calculo del problema del morral de forma recursiva')

    print(f'El valor maximo que podemos robar es {resultado}')
    print('La complejidad del algoritmo es O(nW) donde n es el numero de elementos y W el tamano del morral')