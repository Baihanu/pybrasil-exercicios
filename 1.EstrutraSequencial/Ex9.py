"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
fahrenheit = int(input('Por favor informe a temperatura: '))
celsius = (((fahrenheit - 32) / 9) * 5)
print(f'{fahrenheit}º Fahrenheit são equivalentes a {celsius}º Celsius')
