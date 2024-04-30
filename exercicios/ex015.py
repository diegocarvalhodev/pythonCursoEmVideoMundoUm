"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.
"""
quant_km = int(input('Informe o total de quilometros foram percorridos: '))
quant_dias = float(input('Informa o total de dias da locação: '))

valor_a_pagar = (quant_km * 0.15) + (quant_dias * 60.0)

print('O valor total a pagar é R${:.2f}'.format(valor_a_pagar))
