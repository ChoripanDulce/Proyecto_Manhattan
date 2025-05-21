import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Cargar los datos desde el archivo CSV (asegúrate de que el path sea correcto)
df = pd.read_csv("US_FTRI_20230628035959.csv")
df = df[
    (df["Year"].between(2008, 2021)) &
    (df["Economy Label"] == "Colombia") &
    (df["Category Label"] == "Overall index")
]

# Agrupar por año y calcular el promedio del índice global de innovación para Colombia
df_grouped = df.groupby("Year")["Index"].mean().reset_index()

# Crear figura y eje
fig, ax = plt.subplots()
ax.set_xlim(2008, 2021)
ax.set_ylim(df_grouped["Index"].min(), df_grouped["Index"].max())
ax.set_xlabel("Año")
ax.set_ylabel("Índice Global de Innovación")
ax.set_title("Índice Global de Innovación en Colombia (2008-2021)")

# Cambiar el fondo del gráfico a blanco
ax.set_facecolor("white")

# Graficar la línea con marcadores (color naranja) y agregar leyenda
line, = ax.plot([], [], color="orange", marker="o", lw=2, label="Colombia")
ax.legend(loc="upper left")

# Si antes se anotaban valores para ciertos años (por ejemplo, 2008 y 2021) este bloque se elimina
# for year, index in zip(df_grouped["Year"], df_grouped["Index"]):
#     if year in [2008, 2021]:
#         ax.annotate(f"{index:.2f}", (year, index),
#                     textcoords="offset points", xytext=(0, 10), ha="center")

# Función para la animación
def update(frame):
    idx = frame % len(df_grouped)
    line.set_data(df_grouped["Year"][:idx], df_grouped["Index"][:idx])
    return line,

# Crear animación y guardarla como archivo GIF
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(1, len(df_grouped) + 1),
    interval=350, repeat=True
)
ani.save("grafica_colombia.gif", writer="pillow")

