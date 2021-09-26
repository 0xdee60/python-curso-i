class Perro:
    def __init__(self,raza,nombre,puntos):
        self.raza = raza
        self.nombre = nombre

        #este campo es bool
        self.puntos = puntos
    def __str__(self):
        return 'Nombre: '+self.nombre +'\nRaza: '+self.raza+'\nPuntos: '+ str(self.puntos)


huskie = Perro(raza='Huskie',nombre='Pepito',puntos=False)

print(huskie)
