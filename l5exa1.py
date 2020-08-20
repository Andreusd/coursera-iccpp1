import math

def isPrime(n):
    for x in range(2,math.ceil(n/2)+1):
        if(n%x==0):
            return False
    return True

def n_primos(n):
    primos=0
    for i in range(2,n+1):
        if(isPrime(i)):
            primos+=1
    return primos