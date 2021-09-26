def func_es_par(num):
    if(num%2==0):
        return True
    else:
        return False
    
una_lista = [1,2,3,4,5,6,7,8,9,10]

#filtra solo los elementos verdaderos
for item in filter(func_es_par,una_lista):
    print(item)

