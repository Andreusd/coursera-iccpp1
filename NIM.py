def computador_escolhe_jogada(n,m):
    if(m>=n):
        print("O computador tirou",n,"peças")
        return n
    for x in range(n,0,-1):
        if(((n-x)%(m+1)==0) and x<=m):
            print("O computador tirou",x,"peças")
            return x
def usuario_escolhe_jogada(n,m):
    escolha=m+1
    while(escolha>m):
        escolha = int(input("Quantas peças você vai tirar? "))
        if(escolha>m or escolha<1 or (n<m and escolha>n)):
            print("Oops! Jogada inválida! Tente de novo.")
            escolha=m+1
    return escolha

def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    if(n%(m+1)==0):
        print("Voce começa!")
        n=n-usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!")
    while(n>0):
        n=n-computador_escolhe_jogada(n,m)
        if(n<=0):
            break
        n=n-usuario_escolhe_jogada(n,m)
    print("Fim do jogo! O computador ganhou!")
        
def campeonato():
    print("Voce escolheu um campeonato!")
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("Placar: Você 0 X 3 Computador")

    
def inicia():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    escolha = input("2 - para jogar um campeonato ")
    if(escolha==1):
        partida()
    else:
        campeonato()
        
inicia()
