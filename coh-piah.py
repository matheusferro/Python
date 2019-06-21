import re

def le_assinatura():
    #'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    #'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    #'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
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
    #'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #'''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver
    #  o grau de similaridade nas assinaturas.'''
    # Sab=∑i=16||fi,a−fi,b||6
    s = 0
    for traco in range(len(as_a)):
        s = s + abs(as_a[traco] - as_b[traco])
    return s / 6


def calcula_assinatura(texto):
    #'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura 
    # do texto.'''
    sentenca = separa_sentencas(texto)
    li_frase = []
    for x in sentenca:
        frases_separada = separa_frases(x)
        for f in frases_separada:
            li_frase.append(f)
    
    li_palavra = []
    for y in li_frase:
        palavras_separadas = separa_palavras(y)
        for p in palavras_separadas:
            li_palavra.append(p)
    ass = []
    ass.append(tam_m_palavra(li_palavra))
    ass.append(relacao_type_token(li_palavra))
    ass.append(razao_h_l(li_palavra))
    ass.append(tamanho_medio_sentenca(sentenca))
    ass.append(complex_sentenca(li_frase, sentenca))
    ass.append(tam_m_frase(li_frase))
      
    return ass

def avalia_textos(textos, ass_cp):
    #'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver 
    # o numero (1 a n) do texto com maior probabilidade de ter sido infectado 
    # por COH-PIAH.'''
    v = ass_cp[0]
    for x in range(len(ass_cp)):
        if(ass_cp[x] < v):
            v = ass_cp[x]
            i = x
    return i

def relacao_type_token(palavras):
    return n_palavras_diferentes(palavras)/ len(palavras)

def razao_h_l(palavras):
    return n_palavras_unicas(palavras)/ len(palavras)

def tamanho_medio_sentenca(sentencas):
    caracteres_sentenca = 0 
    for s in sentencas:
        caracteres_sentenca = caracteres_sentenca + len(s)
    return caracteres_sentenca / len(sentencas)

def complex_sentenca(li_frases, sentencas):
    return len(li_frases) / len(sentencas)

def tam_m_frase(li_frases):
    caracteres_frase = 0
    for f in li_frases:
        caracteres_frase = caracteres_frase + len(f)
    return caracteres_frase / len(li_frases)

def tam_m_palavra(palavra):
    tam_palavra = 0
    total_palavra = len(palavra)
    for p in palavra:
        tam_palavra = tam_palavra + len(p)
    return tam_palavra / total_palavra

def main():
    ass_principal = le_assinatura()
    texto = le_textos()
    ass = []
    for tx in texto:
        ass.append(calcula_assinatura(tx))
    
    ass_comparada = []
    for assinatura in ass:
        ass_comparada.append(compara_assinatura(ass_principal, assinatura))
    
    infectado = avalia_textos(texto, ass_comparada)
    print('O autor do texto' + infectado + 'está infectado com COH-PIAH')

main()

