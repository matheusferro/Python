num = int(input('Digite um número inteiro: '))
soma = 0
while num != 0:
    ulti= (num % 10)
    soma = soma + ulti
    num = num // 10

print(soma)