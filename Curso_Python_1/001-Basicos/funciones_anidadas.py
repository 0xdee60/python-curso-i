#funciones anidadas
def func_hola():
    name = 'Miguel Fernando'

    def func_saludar():
        print('Hola '+name+', ten un buen dia.')

    #se llama la funcion anidada dentro de la otra funcion
    func_saludar()

#llamamos la funcion hola
func_hola()

print('\n')

#reasignacion local de variables
x = 50 

def func1(x):
    #reasignacion local
    x = 200
    print(f'Fui reasignada a {x}')

func1(x)
print('Valor actual de x: {}'.format(x))

print('\n')
#reasignacion global
def func2():
    global x
    x=300
    print(f'Fui reasignada a {x}')

func2()
print('Valor actual de x: {}'.format(x))

