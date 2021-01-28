class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def anvanza(self):
        print('Ando caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def anvanza(self):
        print('Ando pedaleando')

class Nadador(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def anvanza(self):
        print('Ando nadando')


def run():
    persona = Persona('Cesar')
    persona.anvanza()
    ciclista = Ciclista('Tom')
    ciclista.anvanza()
    nadador = Nadador('Michael')
    nadador.anvanza()

if __name__ == '__main__':
    run()