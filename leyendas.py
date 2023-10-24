import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Trazar las líneas y agregar etiquetas
plt.plot(x, y1, label='Línea 1')
plt.plot(x, y2, label='Línea 2')

# Agregar leyenda al gráfico
plt.legend()

# Personalizar la leyenda
plt.legend(loc='upper right', fontsize='small')

# Mostrar el gráfico
plt.show()