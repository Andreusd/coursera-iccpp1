nomes=['primeira','segunda','terceira','quarta']
notas=[]
tamanho=len(nomes)
for i in range(tamanho):
    notas.append(int(input('Digite a {} nota:'.format(nomes[i]))))
ma=(sum(notas))/tamanho
print('A média aritmética é',ma)

#code by andré uziel
