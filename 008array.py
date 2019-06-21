#array / lista / vetores

lista_de_palavras = ['laranja', 'maça', 'pera', 'uva']
lista_de_numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(lista_de_palavras[0], lista_de_numeros[0], lista_de_numeros[9], lista_de_palavras[3] )

#numeros negativos pega do fim para o inicio
print(lista_de_numeros[-1])

def primo(x):
    fator = 2
    if(x == 2):
        return(True)
    while(x % fator != 0 and fator <= x/2):
        fator += 1
    if(x % fator == 0):
        return False
    else:
        return True

limite = int(input('Limite maximo:'))
n = 2
p = []
while n < limite:
    if primo(n):
        p.append(n)
        print(n, end=', ')
    n += 1

print('Quantidade de números primos:  ', len(p))

