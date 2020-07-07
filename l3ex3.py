numero = int(input("Insira um numero:"))
soma=0
while(numero!=0):
    soma += numero%10
    numero=numero//10
print(soma)
