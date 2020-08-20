def maior_elemento2(lista):
    return max(lista)

def maior_elemento(lista):
    maior = lista[0]
    for elemento in lista:
        if maior < elemento:
            maior = elemento
    return maior
