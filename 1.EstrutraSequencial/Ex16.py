"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
E que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
area = int(input('Por favor informe o tamanho a ser pintado (m²): '))
latas = (area / 3)
valor = (latas * 80)
if type(latas) == float:
    latasb = int(latas) + 1
    valorb = (latasb * 80)
    print(f'Para pintar uma área de {area} m² será necessário a quantia de {latasb} latas de tinta.')
else:
    print(f'Para pintar uma área de {area} m² será necessário a quantia de {latas} latas de tinta.')
    print(f'O valor será de R${valor}')
