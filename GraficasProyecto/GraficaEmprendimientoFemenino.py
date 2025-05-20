import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Cargar el archivo CSV
df = pd.read_csv("Dataset3.csv", sep=';')
df = df.sort_values("Women Entrepreneurship Index", ascending=False).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12, 7))

def animate(i):
    ax.clear()
    ax.bar(df["Country"][:i+1], df["Women Entrepreneurship Index"][:i+1], color='skyblue')
    ax.set_title("Índice de Emprendimiento Femenino por País")
    ax.set_xlabel("País")
    ax.set_ylabel("Índice de Emprendimiento Femenino")
    ax.set_xticklabels(df["Country"][:i+1], rotation=90)
    plt.tight_layout()

anim = FuncAnimation(fig, animate, frames=len(df), interval=700, repeat=False)

# Guardar como GIF
anim.save("EmprendiminetoMujer.gif", writer=PillowWriter(fps=10))
plt.close()