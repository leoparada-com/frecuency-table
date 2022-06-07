import os
os.system('cls')

# Este script crea una lista de numeros enteros aleatorios (data) y construye una tabla de frecuencia para la data 

# ------------------------------------------
# 1. Crea un conjunto de números aleatorios
# ------------------------------------------
import random

A = []
numero_elementos = 100
for k in range(0,numero_elementos):
    r1 = random.randint(1,6)
    A.append(r1)
# https://www.geeksforgeeks.org/python-random-module/

print(A)
# -----------------------------------------------
# 2. Determina el dominio del conjunto de números
# ------------------------------------------------
B = list(set(A))
#print(B)
# ------------------------------------------
# 3. Cuenta cuántos hay de cada uno
# ------------------------------------------
import numpy as np

# OPCION 1: con la libreria np.array
# el enfoque usado es localizar los todos los valores y medir el largo del array creado para obtener su contabilizacion
C = []
for k in B:
    pos = len(np.where(np.array(A) == k)[0])
    C.append(pos)

# OPCION 2: con la libreria collections
# https://youtu.be/03vtzKflwzI
# el enfoque usado es crear un diccionario clave/valor con la variable estadistica y la frecuencia de esta
from collections import Counter
CC = dict(Counter(A))

print(CC)

# ------------------------------------------
# 4. Crea una tabla de frecuencia
# ------------------------------------------

from tabulate import tabulate

# usando la opcion 1
D = {'X': B,'F': C}
table_headers = D.keys()
print(tabulate(D, headers=table_headers, tablefmt="psql"))

# usuando la opcion 2
D = {'X': CC.keys(),'F': CC.values()}
table_headers = D.keys()
print(tabulate(D, headers=table_headers, tablefmt="psql"))










