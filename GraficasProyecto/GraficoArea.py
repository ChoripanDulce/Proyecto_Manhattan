import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos ficticios (simulando años 2015-2023)
data = {
    'Año': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Emprendimiento': [30, 35, 42, 50, 60, 65, 70, 75, 80],  # % de crecimiento
    'Innovación': [20, 25, 30, 40, 45, 55, 60, 65, 70]      # % de crecimiento
}
df = pd.DataFrame(data)

# Crear gráfico de área
plt.figure(figsize=(10, 6))
plt.fill_between(df['Año'], df['Emprendimiento'], alpha=0.5, label='Emprendimiento', color='#66c2a5')
plt.fill_between(df['Año'], df['Innovación'], alpha=0.5, label='Innovación', color='#fc8d62')

# Personalización
plt.title('Comparación: Emprendimiento vs. Innovación en Colombia (2015-2023)', fontsize=14)
plt.xlabel('Año')
plt.ylabel('Crecimiento (%)')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('GraficoArea.jpg')
plt.show()