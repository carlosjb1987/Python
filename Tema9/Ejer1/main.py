
lista=[]
pais=""

def introducirLista(pais):
    pais = input("Introduce un país: ")
    lista.append(pais)
    return lista

introducirLista(pais)
introducirLista(pais)
introducirLista(pais)
introducirLista(pais)

resultado = sorted(lista)
print(resultado)