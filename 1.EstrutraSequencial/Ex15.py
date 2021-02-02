"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
A) salário bruto.
B) quanto pagou ao INSS.
C) quanto pagou ao sindicato.
D) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
```
"""
valor_hora = float(input('Por favor informe o seu valor hora: R$'))
hora_trabalhada = int(input('Por favor informe a quantidade de horas trabalhadas: '))
salario_bruto = (hora_trabalhada * valor_hora)
ir = (salario_bruto * 0.11)
inss = (salario_bruto * 0.08)
sindicato = (salario_bruto * 0.05)
salario_liquido = (salario_bruto - ir - inss - sindicato)
print(f'+ Salário Bruto : R${salario_bruto}')
print(f'- IR (11%) : R${ir}')
print(f'- INSS (8%) : R${inss}')
print(f'- Sindicato (5%) : R${sindicato}')
print(f'= Salário Líquido : R${salario_liquido}')
