import math
a=int(input())
b=int(input())
c=int(input())
delta=b**2-4*a*c
if(delta<0):
    print("esta equação não possui raízes reais")
else:
    x1=-b+math.sqrt(delta)/2*a
    if(delta==0):
        print("a raiz desta equação é",x1)
    else:
        x2=-b-math.sqrt(delta)/2*a
        if(x1>x2):
            x1, x2 = x2, x1
        print("as raízes da equação são",x1,"e",x2)
