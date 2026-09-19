from os import system
system ('cls')

# inicia a contagem do multiplicando
for i in range(1,11):
    # limpa a variável "linha"
    linha = ''
    for ii in range(1,11):
        # vai armazenando toda a tabuada
        # ": >4" totaliza 4 caracteres, completando com espaços a esquerda, para alinhar os resultados
        linha += f'{i*ii: >4} '
     # mostra os resultados da tabuada do "multiplicando"
    print(linha)