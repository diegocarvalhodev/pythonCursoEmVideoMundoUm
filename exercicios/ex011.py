"""
Exercício Python 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².
"""
import math

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

qtd_tinta = area / 2

print('Serão necessários {} litro(s) de tinta para pintar uma parede com {}m².'.format(qtd_tinta, area))
