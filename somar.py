# Receber 2 numeros do usuário, realizar a soma entre eles e exibir
# int = transforma texto em um numero inteiro
num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
soma = num1 + num2

# print('A soma entre', num1 , 'e' , num2 , 'é de', soma)
print('A soma entre {} e {} é de {}' . format(num1,num2, soma))