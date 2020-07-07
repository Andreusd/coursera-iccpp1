import math
primo=True
numero = int(input("Insira um numero:"))
if(numero==1):
    primo=False
for i in range(2,math.ceil(math.sqrt(numero))+1):
    if(numero%i==0):
        primo=False

if(primo):
    print("primo")
else:
    print("não primo")
