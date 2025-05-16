import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Cargar los datos desde el archivo CSV
df = pd.read_csv("US_FTRI_20230628035959.csv")  # Reemplaza con el nombre correcto de tu archivo
df = df[df["Year"].between(2008, 2021)]  # Filtrar años relevantes

# Agrupar por año y calcular el promedio del índice global de innovación
df_grouped = df.groupby("Year")["Index"].mean().reset_index()

fig, ax = plt.subplots()
ax.set_xlim(2008, 2021)
ax.set_ylim(df_grouped["Index"].min(), df_grouped["Index"].max())
ax.set_xlabel("Año")
ax.set_ylabel("Índice Global de Innovación")
ax.set_title("Evolución del Índice Global de Innovación (2008-2021)")

# Cambiar el fondo del gráfico
ax.set_facecolor('#f0f0f0')  # Fondo gris claro

# Agregar una cuadrícula
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Cambiar el estilo de la línea y agregar marcadores
line, = ax.plot([], [], 'r-o', lw=2, label="Índice de Innovación")  # Línea roja con marcadores circulares

# Agregar una leyenda
ax.legend(loc="upper left")

# Agregar anotaciones en puntos clave
for year, index in zip(df_grouped["Year"], df_grouped["Index"]):
    if year in [2008, 2021]:  # Anotar solo los años inicial y final
        ax.annotate(f'{index:.2f}', (year, index), textcoords="offset points", xytext=(0, 10), ha='center')

# Función para la animación
def update(frame):
    idx = frame % len(df_grouped)  # Permite la repetición infinita
    ax.set_xlim(2008, 2021)  # Mantener los límites constantes
    line.set_data(df_grouped["Year"][:idx], df_grouped["Index"][:idx])
    return line,

# Crear animación con transiciones suaves y en bucle
ani = animation.FuncAnimation(fig, update, frames=np.arange(1, len(df_grouped) * 2), interval=260, repeat=True)

plt.show()