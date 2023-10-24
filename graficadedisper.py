import matplotlib.pyplot as plt

tiempo_estudio = [1.5, 2.0, 2.5, 1.0, 3.0, 2.5, 4.0, 3.5, 2.0, 1.5]
calificaciones = [60, 65, 75, 55, 80, 70, 85, 75, 60, 50]

plt.scatter(tiempo_estudio, calificaciones, color='blue')
plt.title('Relación entre Tiempo de Estudio y Calificaciones')
plt.xlabel('Tiempo de Estudio diario (horas)')
plt.ylabel('Calificaciones en el examen (porcentaje)')

plt.show()