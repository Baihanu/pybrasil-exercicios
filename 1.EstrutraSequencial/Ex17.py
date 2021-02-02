"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
area = int(input('Por favor informe o tamanho a ser pintado (m²): '))
litros = (area / 6)


lata18 = (litros / 18)
valor_lata = (lata18 * 80)
if type(lata18) == float:
    lata18_b = int(lata18) + 1
    valor_lata_b = (lata18_b * 80)
    print(f'A) Para pintar {area} metros quadrados, serão necessárias {lata18_b} latas, valor total de: R${valor_lata_b}')
else:
    print(f'A) Para pintar {area} metros quadrados, serão necessárias {lata18} latas, valor total de: R${valor_lata}')


galao = (litros / 3.6)
valor_galao = (galao * 25)
if type(galao) == float:
    galao_b = int(galao) + 1
    valor_galao_b = (galao_b * 25)
    print(f'B) Para pintar {area} metros quadrados, serão necessários {galao_b} galões, valor total de: R${valor_galao_b}')
else:
    print(f'B) Para pintar {area} metros quadrados, serão necessárias {galao} latas, valor total de: R${valor_galao}')
