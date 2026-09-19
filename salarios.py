from os import system
system ('cls')

salario_bruto = input('Digite seu salário bruto: ')
salario_bruto = float(salario_bruto.replace(',' , '.'))

if salario_bruto <= 1621:
    desconto = salario_bruto * 0.075 - 0
    salario_posinss = salario_bruto - desconto
    print(' Seu salário pós INSS é de R${} ' . format(salario_posinss))
elif salario_bruto < 2902.84:
    desconto = salario_bruto * 0.09 - 24.32
    salario_posinss = salario_bruto - desconto
    print('Seu salário pós INSS é de R${}' . format(salario_posinss))
elif salario_bruto < 4354.27:
    desconto = salario_bruto * 0.12 - 111.41
    salario_posinss = salario_bruto - desconto
    print(' Seu salário pós INSS é de R${}' . format (salario_posinss))
elif salario_bruto < 8475.55:
    desconto = salario_bruto * 0.14 - 198.50
    salario_posinss = salario_bruto - desconto
    print('Seu salário pós INSS é de R${}' . format(salario_posinss))
else:
    salario_posinss = salario_bruto - 988.07
    print('Seu salário pós INSS é de R${}' . format(salario_posinss))

if salario_posinss <= 2428.80:
    desconto = salario_posinss - 0
    print('Seu salário líquido é de R${}' . format(salario_posinss - desconto))
elif salario_posinss < 2826.65:
    desconto = salario_posinss * 0.075 - 182.16
    print('Seu salário líquido é de R${}' . format(salario_posinss - desconto))
elif salario_posinss < 3751.05:
    desconto = salario_posinss * 0.15 - 394.16
    print('Seu salário líquido é de R${}' . format(salario_posinss - desconto))
elif salario_posinss < 4664.68:
    desconto = salario_posinss * 0.225 - 675.49
    print('Seu salário líquido é de R${}' . format(salario_posinss - desconto))
else:
    desconto = salario_posinss * 0.275 - 908.72
    print('Seu salário líquido é de R${}' . format(salario_posinss - desconto))
