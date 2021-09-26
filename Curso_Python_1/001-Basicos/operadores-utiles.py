from random import shuffle, randint #importando funcion shuffle y randint del modulo random 

print(list(range(0,11,2))) #crear lista del 0 al 11 (11-1) con 2 saltos

#imprimir valores de una lista
contador_indice = 0

palabra='Hola'

for indice,letra in enumerate(palabra):
    print(indice,letra,'\n')



#juntar clave valor de dos listas
mi_lista1 = [1,2,3]
mi_lista2 = ['a','b','c']

for item in zip(mi_lista1,mi_lista2): #zip empareja las listas de parentesis
    print(item)

mi_lista3 = list(zip(mi_lista1,mi_lista2))
print(mi_lista3)

if 'a' in mi_lista2:
    print(True)

print(min(mi_lista1)) #iprimir valor menor de la lista

print(max(mi_lista1)) #imprimir valor maximo de la lista
print(mi_lista1)

shuffle(mi_lista1) #mescla lista 

print(mi_lista1)

x = randint(1,100)
print(x)

z = float(input('Igresa un numero: ')) #ingresar valores
print(z)

