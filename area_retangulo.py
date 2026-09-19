#Calcular a área de um retangulo
# float = ponto flutuante, ou seja, aceita casas decimais
base = (input('Informe a medida da base: '))
altura = (input('Inforeme a medida da altura: '))

# Valida se a Base e a Altura são numéricos
print('Base é numérico? ', base.isnumeric())
print('Altura é numérico?', altura.isnumeric())

# Calcula a área do retangulo
area = float(base)*float(altura)

# print('A multiplicação entre {} e {} é de {}' . format(base, altura, multiplicação))
print('A Àrea do retangulo é de;' , area)