# Gere uma matriz 2x5 e mostre:
# número de dimensões
# formato (shape)
# quantidade total de elementos (size).
import numpy as np
import os
os.system('clear')

rng = np.random.default_rng()

numeros = np.random.randint(1, 11, size=(2, 5))

print(f'Matriz:\n{numeros}\n')
print(f'Número de dimensões: {numeros.ndim}')
print(f'Shape: {numeros.shape}')
print(f'Tamanho: {numeros.size}')