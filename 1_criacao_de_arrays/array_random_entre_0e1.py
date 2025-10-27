# Crie um array com 10 números aleatórios entre 0 e 1.
import numpy as np
import os
os.system('clear')

rng = np.random.default_rng()

numeros = rng.random(size=5)
print(numeros)