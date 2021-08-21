
# Generar un numero aleatorio
import random
print(random.randint(1, 20))

import random
print(random.randrange(10, 100, 2))

# Reacomodar una lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original", lista)

random.shuffle(lista)

print("Lista mixeada", lista)

# Instalar 
# python -m pip install -U pip
# python -m pip install -U matplotlib

import matplotlib.pyplot as plt

# Genera una grafica de Campana de Gauss
campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()