"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
print('Olá, por favor siga as instruções abaixo')
nota1 = float(input('Por favor informe a nota do primeiro bimestre: '))
nota2 = float(input('Por favor informe a nota do segundo bimestre: '))
nota3 = float(input('Por favor informe a nota do terceiro bimestre: '))
nota4 = float(input('Por favor informe a nota do quarto bimestre: '))
media = ((nota1 + nota2 + nota3 + nota4) / 4)
print(f'A media das notas {nota1}, {nota2}, {nota3} e {nota4} é:', media)
