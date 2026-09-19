from os import system
system ('cls')

# calculo de IMC
altura = input('Digite a sua altura em metros: ')
altura = float(altura.replace(',' , '.'))
# substitui o ponto em vírgula

peso = (input('Digite seu peso em KG: '))
peso = float(peso.replace(',' , '.'))

# imc = peso / altura ** 2
imc = peso / (altura * altura)

# 
# print('Seu IMC:  {}' . format(imc))
print(f'Seu IMC: {imc:.2f}')

if imc < 18.5:
    print('Voce esta baixo do peso normal')
elif imc < 25:
    print('Voce esta com o peso ideal')
elif imc < 30:
    print('Voce esta com excesso de peso')
elif imc < 35:
    print('Voce tem obesidade classe 1')
elif imc < 40:
    print('Voce tem obesidade classe 2')
elif imc >= 40:
    print(' voce tem obesidade classe 3')
 