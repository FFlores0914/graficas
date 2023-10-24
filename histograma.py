import matplotlib.pyplot as plt

edades = [22, 25, 30, 33, 35, 38, 40, 40, 42, 45, 48, 50, 52, 55, 60, 62, 65, 70, 72, 75]

plt.hist(edades, bins=5, edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

plt.show()