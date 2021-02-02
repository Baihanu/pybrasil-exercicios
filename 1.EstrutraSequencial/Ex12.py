"""
Tendo como dados de entrada a altura de uma pessoa.
Construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Por favor, informe sua altura: '))
altura_alt = (altura / 100)
peso_ideal1 = ((altura * 72.7) - 58)
peso_ideal2 = ((altura_alt * 72.7) - 58)

if altura > 3:
    print(f'O peso ideal para uma pessoa que mede {altura_alt} metros é de {peso_ideal2}Kgs')
else:
    print(f'O peso ideal para uma pessoa que mede {altura} metros é de {peso_ideal1}Kgs')
