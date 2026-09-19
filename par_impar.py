from os import system
system("cls")

numero = int(input('Digite um número: '))
# porcentagem em calculo faz a divisão e retorna o RESTO da divisão
resto = numero % 2

# == para comparar valores
# != para comparar valores DIFENTES
# < para comparar valores MENORES
# <= para comparar valores MENORES ou IGUAIS
# > para comparar valores MAIORES
# >= para comparar valores MAIORES ou IGUAIS

if resto == 0:
    print('O número {} é PAR!' . format(numero))
else:
    print('O número {} é IMPAR!' . format(numero))
  