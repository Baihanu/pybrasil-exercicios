"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Por favor informe sua altura em centímetros: '))
h = (altura / 100)
sexo = int(input('Por favor informe seu sexo, 1 para homem, 2 para mulher: '))
if sexo == 1:
    peso_ideal_1 = ((h * 72.7) - 58)
    print(f'O peso ideal para um homem que mede {h} metros é de {peso_ideal_1} Kgs')
elif sexo == 2:
    peso_ideal_2 = ((h * 62.1) - 44.7)
    print(f'O peso ideal para uma mulher que mede {h} metros é de {peso_ideal_2} Kgs')
