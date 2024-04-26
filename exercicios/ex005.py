"""
Exercício Python 005 - Faça um programa que leia um número inteiro e mostre na tela
o seu sucessor e o seu antecessor.
"""

n = int(input('Digite um número inteiro qualquer: '))

print('O sucesso do número {} é {}'.format(n, n + 1))
print('O antecessor do número {} é {}'.format(n, n - 1))
