# Crie um array de 10 elementos e substitua os valores nas posições 3 a 6 por zero.
import numpy as np
import os
os.system('clear')

rng = np.random.default_rng()

numeros = np.random.randint(1, 11, size=10)

print(f'Array original: {numeros}')
numeros[3:7] = 0
print(f'Array fatiada: {numeros}')
