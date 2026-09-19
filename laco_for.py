from os import system
import time
system ('cls')

numero = int(input('Informe um número maior que 0: '))

# Verificar se o número é positivo
if numero <= 0:
    print('NÚMERO INVÁLIDO!')
else:
    # Iniciando Laço For
    for i in range(numero):
        print(f'Valor de variável i: {i}')
        time.sleep(2) #doem por 2 segundos