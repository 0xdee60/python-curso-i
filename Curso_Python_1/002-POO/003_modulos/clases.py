class Animal():
    def __init__(self):
        print('Animal creado')

    def quien_soy(self):
        print('soy un animal...')
    
    def comer(self):
        print('Estoy comiendo...')


class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Perro creado')
    def quien_soy(self):
        print('Soy un perro')
    def comer(self):
        print('Estoy comeindo... Soy carnivoro.')