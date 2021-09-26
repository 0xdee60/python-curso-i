vida = 100 

danio = 25

print(vida-danio)
print('\nTipo de dato de vida: ',type(vida))

cadena = "Hola esta es una cadena ' con comilla"

#slicing
print(len(cadena))
print(cadena[3]) #indexado
print(cadena[-1]) #indexado inverso
print(cadena[0:4]) #slicing desde el 0 hasta el 4
print(cadena[0:30:2]) #slicing desde el 0 hasta el 30 realizando 2 saltos
print(cadena[::]) #slicing desde el inicio hasta el fin


#inmutavilidad de las cadenas de texto
nombre = "Miguel"
print('S'+nombre[1:len(nombre)]) #con , agrega un espacion con + concatena sin espacio
nuevo_nombre='Dark'+nombre[2:len(nombre)]
print(nuevo_nombre)

#a mayusculas y viseversa
minusculas = "este es un texto en minusculas"
print(minusculas.upper())
mayusculas = "ESTE ES UN TEXTO EN MAYUSCULAS"
print(mayusculas.lower())

#dividir cadenas por un caracter
cadena_a_dividir = 'Hola|Mundo|Esta|Es|Una|Cadena'
cadena_dividida = cadena_a_dividir.split('|')
print('Cadena dividida: '+str(cadena_dividida))

#formato de impresion de cadenas de texto(interpolacion de cadenas)
print('Esta {} una {} de {}'.format('ES','CADENA','TEXTO'))
print('Esta {0} una {0} de {0}'.format('ES','CADENA','TEXTO'))
print('Esta {0} una {1} de {2}'.format('ES','CADENA','TEXTO'))
print('Esta {c} una {b} de {a}'.format(a='ES',b='CADENA',c='TEXTO'))

#cambiar representacion de numeros float
numero_float = 100/888
print('El numero float es {}'.format(numero_float))
print('El numero float es {r}'.format(r=numero_float))
print('El numero float es {r:10.3f}'.format(r=numero_float)) #{valor:width.presicion f}
print('El numero float es {r:1.5f}'.format(r=numero_float)) #{valor:width.presicion f}

#interpolacion de cadenas con fstrings
fst_nombre = "Mike"
fst_edad = 22
print(f"Su nombre es {fst_nombre} y tiene {fst_edad} anios.")