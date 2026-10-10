from os import system
import math

system('cls')

# Um transporte ?? toneladas de carga
# Quantas viagens ele precisa fazer somente com capacidade maxima

capacidade_total = int(input('Carga total (em toneladas): '))
carga_viagem = float(input('Carga para viagem (em toneladas): '))

quantidade_viagens = math.floor(carga_viagem / capacidade_total)
carga_restante = carga_viagem - (capacidade_total * quantidade_viagens)

print(f'Quantidade de viagens carga máxima: {quantidade_viagens}')
print(f'Carga restante: {carga_restante:.2f} toneladas')