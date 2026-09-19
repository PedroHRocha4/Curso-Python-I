from os import system
system("cls")

# Funções para trabalhar com textos
nomecompleto = input("Digite seu nome completo: ")

# len = length - conta o número dee caracteres
print("- Função para contar caracteres: ", len(nomecompleto))
# upper = tranforma texto em maiusculo
print("- Função para texto maiusculo ", nomecompleto.upper())
# lower = transforma texto em minusculo
print("- Função para texto minusculo ", nomecompleto.lower())
# capitalize = transforma a primeira letra do texto em maiusculo
print("- Função para primeiro maiusculo: ", nomecompleto.capitalize())
# title = transforma a primeira letra de cada palavra em maiusculo
print("- Função para primeira letra de cada palavra maiuscula: ", nomecompleto.title())
# strip = remove os espaços em branco antes e depois do texto
print("- Função para remover espaços antes e depois do texto: ", nomecompleto.strip())
# find = encontrar a posição do caracter
espaço = nomecompleto.find(" ")
print("- Primeira letra: ", nomecompleto[0:espaço])
# replace = buscar e substituir texto
print("- Remover espaços vazio: ", nomecompleto.replace(" ",""))
print("- Contar letras sem espaço: " , len(nomecompleto.replace(" ", "")))