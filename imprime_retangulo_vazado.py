l = int(input('digite a largura: '))
a = int(input('digite a altura: '))
y = 1
x = 0
while y <= a:
    while x < l:
        if(x >= 1 and y != 1 and x != (l-1) and y != a):
            print(end=' ')
            x += 1
        else:
            print('#', end='')
            x += 1
    y += 1
    print()
    x = 0
