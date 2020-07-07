adjacente=False
numero = int(input("Insira um numero:"))
anterior=numero%10
while(numero!=0):
    numero=numero//10
    atual=numero%10
    if(atual==anterior):
        adjacente=True
    anterior=numero%10
if(adjacente):
    print("sim")
else:
    print("nao")
