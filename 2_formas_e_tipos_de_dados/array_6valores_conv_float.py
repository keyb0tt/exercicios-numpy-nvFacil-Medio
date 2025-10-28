# Gere um array com 6 valores e converta-o para o tipo float.
import numpy as np
import os
os.system('clear')

rng = np.random.default_rng()

valores_int = rng.integers(1, 11, size=6)
valores_float = valores_int.astype(float)

print(valores_int)
print(valores_float)