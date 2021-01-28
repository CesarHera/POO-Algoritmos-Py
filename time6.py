import time
import sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 998

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)


# print(sys.getrecursionlimit())
# Antes de utilizarlo deberás hacer un import del modulo sys, al comienzo de tu script:

# import sys
# Para ampliar este limite debes hacer un:

# sys.setrecursionlimit(numero_limite)

# Compañeros, en palabras sencillas, no les funciona porque están demandando más memoria que la que su computadora puede darles 😃