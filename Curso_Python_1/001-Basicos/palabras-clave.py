x = "Hola mundo"

for item in x:
    #si no se coloca nada se generara un error
    pass #se usa para evitar ese error
print(x)

for item in x:
    if item == 'H':
       continue #evita este paso cuando encuentra una H
    print(item)