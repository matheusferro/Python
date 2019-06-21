def fatorial (n)
    fat = 1
    while (n > 1):
            fat = fat * n
            n = n - 1
    return fat

def coeficiente_binominal (n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))
    
n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))
print(coeficiente_binominal(n, k))