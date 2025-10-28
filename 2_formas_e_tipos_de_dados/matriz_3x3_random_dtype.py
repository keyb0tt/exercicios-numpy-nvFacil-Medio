# Crie uma matriz 3x3 com valores inteiros aleatórios e exiba seu tipo (dtype).
import numpy as np
import os
os.system('clear')

rng = np.random.default_rng()

numeros_aleatorios = rng.integers(1, 50, size=5)

print(numeros_aleatorios)
print(numeros_aleatorios.dtype)