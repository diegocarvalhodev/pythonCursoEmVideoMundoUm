n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, mult, div), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
