import math
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

delta = (b**2)-4*a*c
if delta > 0:
    print('as raízes da equação são', (-b+math.sqrt(delta))/2*a, ' e ', (-b-math.sqrt(delta))/2*a)
elif delta == 0:
    print('a raiz desta equação é', (-b+math.sqrt(delta))/2*a)
elif delta < 0:
    print('esta equação não possui raízes reais')
else: 
    print('Digite números válidos')