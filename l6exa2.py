numero = int(input())
lista = []
while numero > 0:
    lista.append(numero)
    numero = int(input())
for elemento in lista[::-1]:
    print(elemento)
