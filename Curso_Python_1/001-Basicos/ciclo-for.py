#100 veces hola
for n in range(0,10):
    print(n+1," Hola mundo")

mi_lista = [1,2,3,4,5,6]

print('\n\n')
for item in mi_lista:
    print(item)

print('\n\n')
for item in mi_lista:
    if(item%2 == 0):
        print('par: '+str(item))
    else:
        print('impar: '+str(item))


print('\n\n')
suma = 0
for item in mi_lista:
    suma += item

print('La suma total es: '+str(suma))

#como despaquetar tuplas
lista_ejem = [(1,2),(3,4),(5,6),(7,8)]
print(len(lista_ejem))
for (a,b) in lista_ejem:
    print(a)
    print(b)

#ciclo for atravez de un diccionario
mi_diccionario = {'a':1,'b':2,'c':3}
for item in mi_diccionario.items():
    print(item)

for item in mi_diccionario.values():
    print(item)

for llave,valor in mi_diccionario.items():
    print('llave: ', llave, 'valor: ', valor)

