#Aprendendo comando for

"""for x in range(1, 100):
    print(x)"""
    
div = 0    
a = int(input('Entre com um número: '))
for x in range (1, a+1):
    resto = a % x
    if resto == 0:
        div = div +1
if div == 2:
    print('Número {} é primo' .format(a))
else:
    print('Número {} não é primo' .format(a))
    