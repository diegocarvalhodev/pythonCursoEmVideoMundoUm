nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:<20}!'.format(nome))  # Alinhado a esquerda com 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))  # Alinhado a direita com 20 caracteres
print('Prazer em te conhecer {:^20}!'.format(nome))  # Centralizado com 20 caracteres
print('Prazer em te conhecer {:#^20}!'.format(nome))  # Centralizado com 20 caracteres preenchidos com #
