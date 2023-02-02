#condicionais

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}' .format(a))
elif b > a and b > c:
    print('O maior número é {}' .format(b))
else:
    print('O maior número é o {}' .format(c))
print('Fim do programa')

#ver se o número é par
a = int(input('Entre com um valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a ==0 or resto_b == 0:
    print('Foi digitado um número par')
else:
    print('Nenhum número par foi digitado')

    #verificador condicional negativa

    a = int(input('Entre com um valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a ==0 or not resto_b > 0:
    print('Foi digitado um número par')
else:
    print('Nenhum número par foi digitado')

#calcular média do aluno e validar com uma mensagem

nota1 = float(input('Primeiro bimestre: '))
nota2 = float(input('Segundo bimestre: '))
nota3 = float(input('Terceiro bimestre: '))
nota4 = float(input('Quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print('media: {}' .format(media))
else:
    print('Foi informada alguma nota errada')  

#Outra forma de apresentar a média

nota1 = float(input('Primeiro bimestre: '))
if nota1 > 10:
    nota1 = float(input('Você digitou errado. Primeiro bimestre: '))
nota2 = float(input('Segundo bimestre: '))
if nota2 > 10:
    nota2 = float(input('Você digitou errado. Segundo bimestre: '))
nota3 = float(input('Terceiro bimestre: '))
if nota3 > 10:
    nota3 = float(input('Você digitou errado. Terceiro bimestre: '))
nota4 = float(input('Quarto bimestre: '))
if nota4 > 10:
    nota4 = float(input('Você digitou errado. Quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print('media: {}' .format(media))
else:
    print('Foi informada alguma nota errada')
