"""
Exercício Python 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
n = int(input('Digite um número: '))

print('O dobro do número {} é {}'.format(n, n * 2))
print('O triplo do número {} é {}'.format(n, n * 3))
print('A raiz quadrada de {} é {}'.format(n, int(n ** 0.5)))
