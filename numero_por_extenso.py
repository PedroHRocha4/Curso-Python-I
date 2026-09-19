from os import system
system('cls')

numeros = ('zero', 'um', 'dos', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezena = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

numero = int(input('Digite um número entre 0 e 99: '))

if numero >= 0 and numero <= 99:

    if numero < 10:
        print(numeros[numero])
    elif numero < 20:
        print(dez[numero-10])
    

else:
    print('Número inválido')