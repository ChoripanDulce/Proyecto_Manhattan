import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar el archivo CSV con el separador correcto
df = pd.read_csv("Dataset3.csv", sep=';')

# Ordenar por índice de emprendimiento femenino (opcional)
df = df.sort_values("Women Entrepreneurship Index", ascending=False)

# Crear gráfico de barras
plt.figure(figsize=(12, 7))
plt.bar(df["Country"], df["Women Entrepreneurship Index"], color='skyblue')
plt.title("Índice de Emprendimiento Femenino por País")
plt.xlabel("País")
plt.ylabel("Índice de Emprendimiento Femenino")
plt.xticks(rotation=90)
plt.tight_layout()


plt.savefig('grafico.jpg')
plt.show()

