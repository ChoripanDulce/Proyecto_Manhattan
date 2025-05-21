import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

# Datos ficticios (simulando años 2015-2023)
data = {
    'Año': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Emprendimiento': [30, 35, 42, 50, 60, 65, 70, 75, 80],  # % de crecimiento
    'Innovación': [20, 25, 30, 40, 45, 55, 60, 65, 70]      # % de crecimiento
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6)) 

def animate(i):
    ax.clear()
    ax.fill_between(df['Año'][:i+1], df['Emprendimiento'][:i+1], alpha=0.5, label='Emprendimiento', color='#66c2a5')
    ax.fill_between(df['Año'][:i+1], df['Innovación'][:i+1], alpha=0.5, label='Innovación', color='#fc8d62')
    ax.set_title('Comparación: Emprendimiento vs. Innovación en Colombia (2015-2023)', fontsize=14)
    ax.set_xlabel('Año')
    ax.set_ylabel('Crecimiento (%)')
    ax.legend(loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlim(df['Año'].min(), df['Año'].max())
    ax.set_ylim(0, max(df['Emprendimiento'].max(), df['Innovación'].max()) + 10)

anim = FuncAnimation(fig, animate, frames=len(df), interval=600, repeat=False)
anim.save('GraficoArea.gif', writer=PillowWriter(fps=1))
plt.close() 