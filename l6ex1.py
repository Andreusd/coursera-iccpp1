def remove_repetidos(lista):
    lista=list(set(lista))
    lista.sort()
    return lista

def remove_repetidos2(lista):
    usados=[]
    for elemento in lista:
        if(elemento not in usados):
            usados.append(elemento)
    usados.sort()
    return usados
