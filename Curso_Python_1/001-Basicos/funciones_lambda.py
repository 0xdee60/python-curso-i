numeros = [1,2,3,4,5,6,7]

#imprimir los pares una lista => filtrar =>lambda variable(item) : condicion, lista a evaluar
print(list(filter(lambda num : num%2==0, numeros)))

#imprimir los numeros al cuadrado lista => mapear =>lambda variable(item) : operacion, lista a operar
print(list(map(lambda numero : numero ** 2, numeros )))

