"""
Exercício Python 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('A média dos números {} e {} é {}'.format(nota1, nota2, media))
