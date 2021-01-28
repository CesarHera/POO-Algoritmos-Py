class CasillaDeVotacion:

    def __init__(self, id, pais):
        self._id = id
        self._pais = pais
        self._region = 'Guadalajara'

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, nueva_region):
        if nueva_region in self._pais:
            print(f'Modificando región {self._region} por {nueva_region}')
            self._region = nueva_region
        else:
            raise ValueError(f'{nueva_region} no se admite en el país')
        
    @region.deleter
    def region(self):
        print(f'Borrando región {self._region}')
        self._region = None
    

voto = CasillaDeVotacion(123, ['Ciudad de México', 'Guadalajara', 'Hidalgo', 'Cancún'])
print(voto.region)
voto.region = 'Cancún'
del voto.region
print(voto.region)
voto.region = 'Hidalgo'