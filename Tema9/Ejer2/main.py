from functools import reduce


lista=[1,2,3,4,5,6,7,8,9,10,11,12,13]

def impares (x):
    if not x % 2 == 0:
        return True

numerosImpares= filter(impares, lista)
numerosImpares=list(numerosImpares)
print (numerosImpares)

def add(a, b):
    return a + b

print(reduce(add, list(numerosImpares))) 


