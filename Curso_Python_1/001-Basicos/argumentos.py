#argumentos posicionales 
def mi_funcion(a:float,b:float):
    #retornar el 5% de la suma de a y b
    #sum resive una tupla, lista, o elemento iterable
    return print(sum([a,b]) * 5 / 100)

#definir una tupla como argumentos los args trabajan como tuplas
def mi_funcion2(*args:float):
    return print((sum(args)) * 5 / 100)

mi_funcion(1,2)
mi_funcion2(60,40,100)

#**kwargs recibe un diccionario
def seleccionar_fruta(**kwargs):
    if('Fruta') in kwargs:
        print('Mi fruta escogida es {}'.format(kwargs['Fruta']))
    else:
        print('No hay fruta')

seleccionar_fruta(Fruta='Pera',Vegetal='Lechuga')

#*args y **kwargs juntos
def precio_comida(*args,**kwargs):
    print(args)
    print(kwargs)

    print('El precio de {} es de {} soles a nombre de {}'.format(args[0],kwargs['Comida'],kwargs['Cliente']))

precio_comida("Pera","Masana","Arroz",Comida=50.00,Cliente='Carlos')




