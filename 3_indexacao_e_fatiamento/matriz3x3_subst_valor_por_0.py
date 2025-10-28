# Gere uma matriz 3x3 com números aleatórios e substitua todos os valores menores que 0.5 por 0.
import numpy as np
import os
os.system('clear')

numeros = np.random.rand(3, 3)

print(f'Matriz original:\n{numeros}\n')

condicao = numeros < 0.5
numeros[condicao] = 0

print(f'Matriz alterada:\n{numeros}\n')
