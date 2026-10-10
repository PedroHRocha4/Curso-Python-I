from os import system
import math

system('cls')

# uma loja precisa armazenar seus produtos em caixas
# Cada caixa pode contar no maximo ?? produtos

num_produtos = int(input('Informe o número de produtos: '))
produtos_caixa = int(input('Informe a quantidade de produtos por caixa: '))

quantidade_caixas = math.ceil(num_produtos / produtos_caixa)
print(f'Caixas necessarias: {quantidade_caixas}')