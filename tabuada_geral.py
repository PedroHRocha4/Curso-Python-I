from os import system
system ('cls')
import time

# inicia contagem do "multiplicando"
for i in range(1,11):
    print(f'Tabuada do {i}:')
    # inicia contagem do "multiplicador"
    for ii in range(1,11):
        print(f'{i} x {ii} = {i*ii}')
        # monta a expressão da multiplicação
        time.sleep(0.10)
    print('')
  


