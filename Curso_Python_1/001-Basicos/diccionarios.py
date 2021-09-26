mi_diccionario = {"ES":"Espania","PE":"Peru","COL":"Colombia"}
print(mi_diccionario)
print(mi_diccionario["COL"]) #llamar valor con llave

segundo_diccionario = {"uno":"5.90","dos":['Pera','Manzana','Melon']}
print(segundo_diccionario["dos"]) #se pueden incluir listas
print(segundo_diccionario["dos"][0]) #se puede llamar un objeto especifico

segundo_diccionario["Goku"] = "Dragon ball" #se agrega un nuevo elemento
print(segundo_diccionario)

segundo_diccionario["Goku"] = "Evangelion" #sobreescribir elemento
print(segundo_diccionario)

print(segundo_diccionario.keys()) #Mostrar solo llaves
print(segundo_diccionario.values()) #Mostrar solo valores

print(segundo_diccionario.items()) #Mostrar lalves y valores


