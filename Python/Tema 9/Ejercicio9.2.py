from functools import reduce

def num(lista): 
    resultado = list(filter((lambda x: x % 2), lista)) 
    print("Lista de numeros: \n",resultado)
    
lista = list(range(50))
num(lista)

suma = reduce( (lambda x, y: x + y), lista) 
print("Sumatoria de los elementos: ",suma)
    




