mi_cadena = 'Hola mundo'

mi_lista = []

for letra in mi_cadena:
    mi_lista.append(letra)

print(mi_lista)

mi_lista2 = [x for x in range(0,11)]

print(mi_lista2)


mi_lista2 = [x for x in "Hola mundo xd"]

print(mi_lista2)


#cambiar temperatura
celcius = [0,10,20,34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]

print(fahrenheit)