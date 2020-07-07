def fatorial(numero):
    if(numero==0):
        return(1)
    return(numero*fatorial(numero-1))

numero = int(input("Insira um numero:"))
print(fatorial(numero))
