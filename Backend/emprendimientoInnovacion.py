import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar el archivo CSV con el separador correcto
df = pd.read_csv("antojitos-para-todos.csv", sep=';')

# Ordenar por índice de emprendimiento femenino (opcional)
df = df.sort_values("Women Entrepreneurship Index", ascending=False)


plt.savefig('GraficoArea.jpg')
plt.show()