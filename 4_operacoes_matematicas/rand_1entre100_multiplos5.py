# Gere um array de 10 números inteiros aleatórios entre 1 e 100 e mostre apenas os múltiplos de 5.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(1, 101, size=10)
condicao = numeros % 5 == 0

print(f'numeros={numeros}\n')
print(f'numeros(multiplos de 5)={numeros[condicao]}\n')

