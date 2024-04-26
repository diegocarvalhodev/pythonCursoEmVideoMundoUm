"""
Exercício Python 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.
"""
salario = float(input('Digite o salário atual do funcionário: R$'))

salario_novo = salario * 1.15   # Salário + 15%

print('\nO salário de R${:.2f} passou para R${:.2f} com o aumento de 15%'.format(salario, salario_novo))
