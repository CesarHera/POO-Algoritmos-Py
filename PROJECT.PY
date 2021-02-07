class Asistente_Financiero_AI:

    def __init__(self):
        self.usuario = 'Cesar'
    # def usuario(self, usuario):
    #     self.usuario = usuario


    def _seleccionador(self, opciones):
        contador = 1
        for i in opciones:
            print(f'{contador}.- {i}')
            contador += 1
        eleccion = input('¿Cuál eliges?: ')
        contador = 1
        for i in opciones:
            if eleccion == str(contador):
                return eleccion
            contador += 1
        
        print(eleccion)
        print("-" * 50)
        print('Elíge una opción correcta | Reiniciando elección...')
        return self._seleccionador(opciones)

    

    def iniciar(self):
        print('---')
        print('MENU PRINCIPAL')
        print('---')
        print(f'¡Bienvenido {self.usuario if self.usuario != None else "."}! ¿En qué te puedo ayudar?')
        eleccion = self._seleccionador(('Definiciones de términos utilizados', 'Elaborar un estado financiero', 'Salir de el programa'))
        if eleccion == '1':
            print('--> Definiciones')
        elif eleccion == '2':
            print('--> Estados financieros')
            self.estados_financieros_menu()
        elif eleccion == '3':
            print('--> Saliendo del programa')

    
    def estados_financieros_menu(self):
        print('---')
        print('MENU DE ESTADOS FINANCIEROS')
        print('---')
        print('Estos son los estados financieros que puedo elaborar por tí:')
        elección = self._seleccionador(('Balance General', 'Estado de cambios en la situación financiera', 'Estado de variaciones en el capital cotable', ))

        if elección == '1':
            print('-->Balance General')
            print("""Antes de iniciar deberas tener listos los siguientes datos: 
📱Activos - Activos circulantes, activos no circulantes, activos diferidos
📱Pasivos - Pasivos circulantes, pasivos no circulantes, pasivos diferidos
📱Capital contable
Si no comprendes algúnos de estos términos te sugiero que vayas a el apartado de <Definiciones> en el programa
O bien si tienes todos los datos listos podemos comenzar""")
            elección = self._seleccionador(('Comenzar', 'Ir al menú principal', 'Elegir otro estado finnciero'))
            if elección == '1':
                print('--> Balance general')
                self.balance_general()
            elif elección == '2':
                print('--> Menú principal')
                self.iniciar()
            elif elección == '3':
                print('--> Menú de estados finncieros')
                self.estados_financieros_menu()

        elif elección == '2':
            print('Ejecutando 2')

        elif elección == '3':
            print('Ejecutando 3')


    def balance_general(self):
        print('Generando balance general')



if __name__ == '__main__':
    print("""Soy una vergota - Proyecto Ascesor Financiero
    Vamos cesar, no te rindas, yo sé que puedes. No claudiques.
    No pares. Recuerdalo, nadie se acuerda de los que se dieron por vencidos.""")

    financiero = Asistente_Financiero_AI()
    financiero.iniciar()