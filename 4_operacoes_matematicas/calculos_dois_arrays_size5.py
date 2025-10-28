# Crie dois arrays de tamanho 5 e realize:
# soma
# subtração
# multiplicação elemento a elemento
# divisão elemento a elemento.
import numpy as np
import os
os.system('clear')

numeros_um = np.random.randint(1, 11, size=5)
numeros_dois = np.random.randint(1, 11, size=5)

numeros_soma = numeros_um + numeros_dois

print(f'numeros_um={numeros_um}')
print(f'numeros_dois={numeros_dois}')