"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
celsius = int(input('Por favor informe a temperatura: '))
fahrenheit = ((celsius * (9/5)) + 32)
print(f'{celsius}º Celsius é equivalente a {fahrenheit}º Fahrenheit')
