def retangulo(l,a):
    for j in range(a):
        for i in range(l):
            if(j==0 or j==a-1):
                print("#",end="")
            elif(i==0 or i==l-1):
                print("#",end="")
            else:
                print(" ",end="")


        print()

l=int(input())
a=int(input())
retangulo(l,a)
