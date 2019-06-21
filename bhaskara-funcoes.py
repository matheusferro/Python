import math
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

def bhaskara (a, b, c):
    return (-b+math.sqrt(delta(a,b,c)))/2*a

def delta (a, b, c):
    return (b**2)-4*a*c

if delta(a,b,c) > 0:
    print('as raízes da equação são', bhaskara(a, b, c), ' e ', bhaskara(a, b, c))
elif delta(a,b,c) == 0:
    print('a raiz desta equação é', bhaskara(a, b, c))
elif delta(a,b,c) < 0:
    print('esta equação não possui raízes reais')
else: 
    print('Digite números válidos')