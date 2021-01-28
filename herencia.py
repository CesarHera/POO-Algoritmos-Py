class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectang = Rectangulo(5, 10)
    print(rectang.area())

    cuadrad = Cuadrado(5)
    print(cuadrad.area())
    
# Cuando la función retorna un valor, necesitamos abrir y cerrar paréntesis para invocarla
# O saldrá un código raro