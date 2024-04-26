"""
Exercício Python 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

Considere US$ 1,00 = R$ 3,27
"""
real = float(input('Digite quanto tem em dinheiro: '))

dolar = real / 3.27

print('\nSeu dinheiro, convertido para dólar, equivale a: {:.2f}'.format(dolar))
