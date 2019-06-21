def campeonato():
    i = 1
    pc= 0
    user= 0
    while i <= 3:
        vencedor = partida()
        if vencedor == 1:
            pc += 1
            i += 1
        else:
            user += 1
            i += 1
    return("Placar: Você {} X {} Computador".format(user,pc))    

def usuario_escolhe_jogada(n,m):
    i = False
    while i != True:
        peca_retirado = int(input('Quantas peças você vai tirar?'))
        if(peca_retirado > m or peca_retirado <= 0):
            peca_retirado = int(input('Quantas peças você vai tirar?'))
        else:
            i = True
            return(peca_retirado)

def computador_escolhe_jogada(n, m):
    print('Vez do computador')
    if(n <= m):
        return m
    else:
        qntd = n % (m+1)
        if(qntd > 0):
            return qntd
        return m

def bemvindo():
    #escolha do tipo de jogo
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('')
    print('1 - para jogar uma partida isolada')
    #pega a escolha 1 ou 2
    escolha = int(input('2 - para jogar um campeonato'))
    #se for 1
    if(escolha == 1):
        partida()
    elif(escolha == 2):
        print(campeonato())

#função main
def partida():
    #pede pro usuario digitar numeros de peças do jogo  o limite permitido para ser retirado
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    #(Tatica vencedora) verifica se o n é multiplo de m+1
            
    if(n % (m+1) == 0):
        print('Você começa')
        i = False
        while i == False:
            peca_user = usuario_escolhe_jogada(n,m)
            if(peca_user > m or peca_user < 0):
                print('Oops! Jogada inválida! Tente de novo.')
                usuario_escolhe_jogada(n,m)
            else:
                n=n-peca_user
            if(n == 0):
                i = True
                print('O usuario ganhou')
                return(2)
            else:
                print('Você tirou', peca_user,' peça(s). Sobrou', n)
                peca_pc = computador_escolhe_jogada(n, m)
                n=n-peca_pc
                if(n == 0):
                    print('O computador retirou ', peca_pc ,' peça(s), sobrou ', n)
                    print('Fim do jogo! O computador ganhou!')
                    return(1)
                else:
                    print('O computador retirou ', peca_pc ,' peça(s), sobrou ', n)
    else:
        print('Computador começa!')
        i = False
        while i == False:
            ppc = computador_escolhe_jogada(n, m)
            n=n-ppc
            if(n == 0):
                i = True
                print('Fim do jogo! O computador ganhou!')
                return(1)
            else:
                print('O computador tirou', ppc,' peça(s). Sobrou', n)
                peca_user = usuario_escolhe_jogada(n,m)
                n=n-peca_user
                if(n == 0):
                    print('O Usuario ganhou')
                    return(2)
                else:
                    print('O usuario retirou ', peca_user ,' peça(s), sobrou ', n)


bemvindo()
