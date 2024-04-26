"""
Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.
"""

temp_celsius = float(input('Digite a temperatura em graus Celsius: '))

temp_fahrenheit = temp_celsius * 9 / 5 + 32

print('A temperatura {}Cº equivale a {}Fº'.format(temp_celsius, temp_fahrenheit))

# (10 °C × 9 / 5) + 32 = 50 °F

