num = int(input('Digite um número'))

indicador = False

while num != 0 and not indicador:
    n = num % 10
    num = num // 10
    n2 = num % 10
    if n == n2:
        indicador = True

if indicador:
    print('tem números adjascentes')
else:
    print(' não tem números adjascentes')