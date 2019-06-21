largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
x = 0
y = 0
while y < altura:
    while x < largura:
        print('#', end='')
        x += 1
    y += 1
    print()
    x = 0
    