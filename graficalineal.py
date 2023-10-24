import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ventas = [120, 150, 135, 170, 200, 250, 220, 240, 280, 300, 280, 320]

plt.plot(meses, ventas, marker='o', linestyle='-', color='blue')
plt.title('Ventas Mensuales')
plt.xlabel('Meses')
plt.ylabel('Ventas (en miles de dólares)')

plt.show()
