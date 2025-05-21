import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

datos = pd.read_csv('antojitos-para-todos.csv', sep=';')

conteo = datos['Localidad'].value_counts()
umbral = 3.7
otros = conteo[conteo / conteo.sum() * 100 < umbral].sum()
conteo_final = conteo[conteo / conteo.sum() * 100 >= umbral].copy()
conteo_final['Otros'] = otros

fig, ax = plt.subplots()
ax.set_title('Distribución de Localidades (Animado)')

def update(frame):
    ax.clear()
    current_data = pd.concat([
        conteo_final.iloc[:frame],
        pd.Series({'Otros': sum(conteo_final.iloc[frame:])})
    ])
    ax.pie(
        current_data,
        labels=current_data.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.tab20.colors
    )
    ax.axis('equal')

ani = FuncAnimation(
    fig,
    update,
    frames=len(conteo_final),
    interval=3000,
    repeat=False
)

ani.save("GraficaTorta.gif", writer=PillowWriter(fps=10))
plt.show()