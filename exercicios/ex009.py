"""
Exercício Python 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
n = int(input('Digite um número: '))

print('{}\n\tTabuada - Soma\n{}'.format('*' * 30, '*' * 30))

for i in range(9):
    print('{} + {} = {}'.format(n, (i + 1), n + (i + 1)))

print('{}\n\tTabuada - Multiplicação\n{}'.format('*' * 30, '*' * 30))

for i in range(9):
    print('{} * {} = {}'.format(n, (i + 1), n * (i + 1)))
