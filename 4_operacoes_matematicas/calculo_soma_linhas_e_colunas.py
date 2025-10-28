# Crie uma matriz 3x3 e calcule a soma das linhas e das colunas separadamente.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(1, 11, size=(3, 3))
print(f'numeros=\n{numeros}\n')

soma_colunas = np.sum(numeros, axis=0)
soma_linhas = np.sum(numeros, axis=1)

print(f'soma_colunas={soma_colunas}')
print(f'soma_linhas={soma_linhas}')