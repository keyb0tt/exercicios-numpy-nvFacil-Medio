# Gere um array de 15 números aleatórios entre 0 e 50.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(0, 51, size=15)
print(f'numeros={numeros}')