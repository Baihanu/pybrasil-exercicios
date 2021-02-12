"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês
"""
valor_hora = float(input('Por favor informe o valor hora: R$ '))
horas_trabalhadas = int(input('Por favor informe a quantidade de horas trabalhadas: '))
salario = (valor_hora * horas_trabalhadas)
print(f'Você receberá R$ {salario} ao final do mês')
