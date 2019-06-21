def cria_matriz(x, y):
    '''X para o valor das colunas, Y para o valor das linhas '''
    matriz = []
    for i in range(y):
        linha = []
        for j in range(x):
            linha.append(int(input('Digite um valor('+ str(i) +')(' + str(j)+ ')')))
        matriz.append(linha)
    return imprime(matriz, y)

def imprime(m, y):
    i = 0
    while i < y:
        print(m[i])
        i += 1

def main():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))

    cria_matriz(lin, col)

if __name__ == "__main__":
    main()