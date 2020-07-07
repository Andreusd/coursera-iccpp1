def maior_primo(x):
    for i in range(x,0,-1):
        primo=True
        for j in range(2,i):
            if(i%j==0):
                primo=False
                break
        if(primo==True):
            return(i)
