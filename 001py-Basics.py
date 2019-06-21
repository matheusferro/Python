print('Hello World')

#assigning values
x = 8 			        #Integer value (int)
y = 9 			        #Integer value (int)
valor_float = 3.14159   #Float value (float)
z = 'python e 10'       #String value (str)

#showing values(You can use "," or "+" or .format())
print(' x =', x)
print(' y ='+ y)
print(' z = {}'.format(z))
print(' float value =',valor_float)

#one way to do a
print('x < y = ', x < y) 			                        

#operacoes

soma = x + y
sub = x - y
divisao = x / y
div_int = x // y 		#Divisao inteira
div_rest = x % y 		#sobra da divisao
pot = x ** 2 			#Potencia
poty = y ** 2 			#Potencia

#PRINT				# A "," serve para concactenar

print('x + y = ', soma)
print('x - y = ', sub)
print('x / y = ', divisao)
print('x // y = ', div_int)
print('x % y = ', div_rest)
print('x ** 2 = ', pot)
print('y ** 2 = ', poty)
print('---- Mostrando todas variaveis ----')
print(x, y, z)

#tipos de variaveis

print('tipo de x= ',type(x))
print('tipo de y= ',type(y))
print('tipo de z= ',type(z))

#converter variaveis
valor_int = int(valor_float)
print('valor float convertido para inteiro', valor_int)

#Tamanho do texto

print('tamanho de z =', len(z))

#nao consigo colocar len(valor_float) pois o len e utilizado somente para string entao converta para string
valor_str = str(valor_float)
print('tamanho do valor float =', len(valor_str))


n = 1j
print('numero complexo', type(n))
