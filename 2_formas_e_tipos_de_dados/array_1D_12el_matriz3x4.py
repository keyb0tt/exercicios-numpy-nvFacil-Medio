# Crie um array 1D com 12 elementos e transforme-o em uma matriz 3x4.
import numpy as np
import os
os.system('clear')

numeros_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f'Array original:{numeros_1d}')

numeros_2d = numeros_1d.reshape(3, 4)
print(f'Array alterada para matriz 3x4:\n{numeros_2d}')

