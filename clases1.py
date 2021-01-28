class Coordenadas:

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def diferencia(self, otra_coordenada):
        diff1 = (self.cord1 - otra_coordenada.cord1) ** 2
        diff2 = (self.cord2 - otra_coordenada.cord2) ** 2

        return (diff1 + diff2) ** 0.5


if __name__ == '__main__':
    coordenadas1 = Coordenadas(8, 80)
    coordenadas2 = Coordenadas(3, 98)

    print(coordenadas1.diferencia(coordenadas2))