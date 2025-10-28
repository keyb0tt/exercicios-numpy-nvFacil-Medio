# Crie um array de 20 elementos e mostre apenas os números pares usando slicing.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(1, 51, size=20)
condicao_pares = numeros % 2 == 0
numeros_pares = numeros[condicao_pares]

print(f'Array original:\n{numeros}\n')
print(f'Números pares:\n{numeros_pares}\n')