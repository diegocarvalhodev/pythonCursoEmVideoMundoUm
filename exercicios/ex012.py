"""
Exercício Python 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
"""
preco_atual = float(input('Digite o preço do produto: '))

preco_com_desconto = preco_atual * 0.95 # Com 5% de desconto

print('\nO preço {}, com desconto de 5%, é {}'.format(preco_atual, preco_com_desconto))
