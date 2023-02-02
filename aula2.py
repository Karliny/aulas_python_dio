a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

#outra forma

a = 10
b = 6
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
print(type(soma))
print('soma: {}, \nsubtracao: {}, \nmultiplicação: {}, \nresto: {}' .format(soma, subtracao, multiplicacao, resto))
#print('subtracao: ' + str(subtracao))
print(multiplicacao)
print(int(divisao))
print(resto)

x = '1'
soma2 = int(x) + 1
print(soma2)


#interação com o usuário
c = int(input('Entre com o primeiro valor: '))
d = int(input('Entre com o segundo valor: '))
soma = c + d
print(soma)