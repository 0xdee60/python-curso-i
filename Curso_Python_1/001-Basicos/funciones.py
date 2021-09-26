def decir_hola():
    print('Hola')
    print('como')
    print('estas')

decir_hola()

def sumar(num1, num2):
    suma=num1+num2
    print('El total es: ', suma)

sumar(1.1,2.5)


def es_par(mi_lista):
    for item in mi_lista:
        if(item%2 == 0):
            print(item,'Es par')
            
        else:
            print(item,'Es impar')
            

mi_lista = [1,2,3,4,5]

es_par(mi_lista)
