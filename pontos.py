import math

x1 = int(input(''))
y1 = int(input(''))

x2 = int(input(''))
y2 = int(input(''))

calculo = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if calculo >= 10:
    print('longe')
else:
    print('perto')

