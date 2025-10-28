# Gere um array de 15 números aleatórios entre 0 e 50.
# Mostre apenas os números maiores que 25.
# Substitua os valores menores que 10 por zero.
# Conte quantos números estão entre 20 e 40.
import numpy as np
import os
os.system('clear')

numeros = np.random.randint(0, 51, size=15)
print(f'numeros =\n{numeros}\n')

numeros_entre_int = numeros[(numeros >= 20) & (numeros <= 40)]
numeros[numeros < 10] = 0

print(f'numeros(substituição ([numeros < 10] = 0)) =\n{numeros}\n')
print(f'numeros > 25 =\n{numeros[numeros > 25]}\n')
print(f'numeros entre 20 e 40 =\n{numeros_entre_int}\n')
print(f'quantidade numeros entre 20 e 40 =\n{len(numeros_entre_int)}\n')
    