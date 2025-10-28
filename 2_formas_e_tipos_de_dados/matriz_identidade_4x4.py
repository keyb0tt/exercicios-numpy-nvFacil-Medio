# Crie uma matriz identidade 4x4.
import numpy as np
import os
os.system('clear')

matriz_identidade = np.zeros((4, 4), dtype=int)
np.fill_diagonal(matriz_identidade, 1)

print(matriz_identidade)
