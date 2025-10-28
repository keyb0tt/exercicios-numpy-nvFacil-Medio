# Gere uma matriz 4x4 e mostre apenas:
# a segunda linha
# a última coluna
# a diagonal principal.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(1, 20, size=(4, 4))

print(f'Matriz:\n{numeros}\n')
print(f'Segunda linha:\n{numeros[1]}\n')
print(f'Última Coluna:\n{numeros[:, -1]}\n')
print(f'Diagonal Principal:\n{np.diagonal(numeros)}\n')