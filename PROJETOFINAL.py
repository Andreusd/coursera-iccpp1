import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve
uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma
lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
similaridade nas assinaturas.'''
    grau=0
    for x in range(len(as_a)):
        if(round(as_a[x],1)==round(as_b[x],1)):
            grau+=1
    return grau

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a
 assinatura do texto.'''
    quantidade_letras=0
    quantidade_palavras=0
    quantidade_sentencas=0
    quantidade_frases=0
    lista_palavras=[]
    quantidade_caracteres_sentenca=0
    quantidade_caracteres_frase=0
    for sentencas in separa_sentencas(texto):
        quantidade_sentencas+=1
        quantidade_caracteres_sentenca+=len(list(sentencas))
        for frases in separa_frases(sentencas):
            quantidade_frases+=1
            quantidade_caracteres_frase+=len(list(frases))
            for palavras in separa_palavras(frases):
                lista_palavras.append(palavras)
                quantidade_palavras+=1
                for letra in palavras:
                    quantidade_letras+=1
    wal = quantidade_letras/quantidade_palavras # tam medio
    quantidade_palavras_diferentes=n_palavras_diferentes(lista_palavras)
    ttr = quantidade_palavras_diferentes/quantidade_palavras
    quantidade_palavras_unicas=n_palavras_unicas(lista_palavras)
    hlr = quantidade_palavras_unicas/quantidade_palavras
    sal = quantidade_caracteres_sentenca/quantidade_sentencas
    sac = quantidade_frases/quantidade_sentencas
    pal = quantidade_caracteres_frase/quantidade_frases
    return wal, ttr ,hlr ,sal, sac, pal

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp
e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido
infectado por COH-PIAH.'''
    graus=[]
    for texto in textos:
        graus.append(compara_assinatura(calcula_assinatura(texto),ass_cp))
    return(graus.index(max(graus)))

def main():
    as_cp=le_assinatura()
    textos=le_textos()
    indice=avalia_textos(textos, as_cp)
    print("O autor do texto",indice,"está infectado com COH-PIAH")
main()
