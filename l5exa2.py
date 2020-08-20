import math

def isHipotenusa(n):
    for i in range(1,20):
        for j in range(1,120):
            if(math.sqrt(i**2+j**2)==n):
                return True
    return False

def soma_hipotenusas(n):
    soma=0
    for i in range(n+1):
        if(isHipotenusa(i)):
            soma+=i
    return soma
