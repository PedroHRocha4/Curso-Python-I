# converter Celsius para Fahrenheit / Kevil
from os import system
system ('cls')

celsius = float(input('Digite a temperatura em Celsius (°C): '))

print('Escolha a temperatura para conversão: ')
print('1 - Fahrenheit (°F)')
print('2 - kelvin (K)')

opcao = int(input('Opção: '))

if opcao == 1:
    farhrenheit = celsius * 1.8 + 32
    print('°C {:.2f} equivale a {:.2f} °F' . format(celsius,farhrenheit))
elif opcao == 2:
    kelvin = celsius + 273.15
    print('°C {:.2f} equivale a {:.2f} K' . format(celsius,kelvin))

else:
      print ('Opção Inválida')

