mi_lista = ["Miguel","Aliaga","Chacon"]
print(mi_lista)
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[2:])
segunda_lista = ["Es","Un","Crack"]

nueva_lista = mi_lista + segunda_lista
print(nueva_lista)

#no son inmutables
nueva_lista[5] = "Programador"
print(nueva_lista)

#agregar elementos a la lista
nueva_lista.append("Confirmoooo")
print(nueva_lista)

#quitar elemento 
item_popeado = nueva_lista.pop()
print(str(nueva_lista)+ ' se elimino: '+item_popeado)

otro_popeado = nueva_lista.pop(2)
print(str(nueva_lista)+' se elimino '+otro_popeado)


#ordenar lista
nueva_lista.sort() #si se iguala a variable da None
print(nueva_lista)

nueva_lista.reverse()
print(nueva_lista)