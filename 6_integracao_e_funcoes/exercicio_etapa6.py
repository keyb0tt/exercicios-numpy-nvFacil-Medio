# Crie uma matriz 5x5 com valores de 1 a 25 (usando arange) e:
# Calcule a soma total
# Mostre a soma da diagonal principal
# Normalize os valores (dividindo todos pelo valor máximo).
import numpy as np
import os
os.system('clear')

numeros = np.arange(1, 26)
numeros_matriz = numeros.reshape(5, 5)

print(f'array numeros:\n{numeros}\n')
print(f'array numeros_matriz:\n{numeros_matriz}\n')