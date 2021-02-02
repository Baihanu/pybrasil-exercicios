"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
num1 = int(input('Por favor informe um número inteiro: '))
num2 = int(input('Por favor informe outro número inteiro: '))
num3 = float(input('Por favor informe um número real: '))
a = ((num1 * 2) * (num2 / 2))
print(f'A) o produto do dobro de {num1} com metade de {num2} é = {a}')

b = ((num1 * 3) + num3)
print(f'B) a soma do triplo de {num1} com {num3} = {b}')

c = (num3 ** 3)
print(f'C) {num3} elevado ao cubo é = {c}')
