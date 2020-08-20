def retangulo(l,a):
    for _ in range(a):
        for _ in range(l):
            print("#",end="")
        print()

l=int(input())
a=int(input())
retangulo(l,a)
