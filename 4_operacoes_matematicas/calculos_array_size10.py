# Crie um array de 10 números e calcule:
# média
# soma
# valor máximo e mínimo
# desvio padrão.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(1, 11, size=10)

print(f'numeros={numeros}')

numeros_soma = np.sum(numeros)
numeros_media = numeros_soma / 10
valor_maximo = max(numeros)
valor_minimo = min(numeros)
desvio_padrao = np.std(numeros)

print(f'\nnumeros_soma={numeros_soma}')
print(f'numeros_media={numeros_media}')
print(f'valor_maximo={valor_maximo}')
print(f'valor_minimo={valor_minimo}')
print(f'desvio_padrao={desvio_padrao}')
