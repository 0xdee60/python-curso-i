#la funcion de mapa es ulti para llenar una funcion con una lista de datos
numeros = [1,2,3,4,5]

def raiz(numero):
    resultado = numero**0.5
    return resultado

#mapea la funcion y los argumentos de numeros 
for item in map(raiz,numeros):
    print(item)


#insertar directamente en una lista
print(list(map(raiz,numeros)))


