import uno 

print("Nivel Top en dos.py")

uno.func1()

#sirve para ver si el modulo ah sido importado
if __name__ == '__main__':
    print('Dos.py esta siendo corrido directamente')

else:
    print('Dos.py Esta siendo importado...')