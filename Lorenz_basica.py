import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos de la curva de Lorenz teórica (distribución perfectamente equitativa)
x = np.linspace(0, 1, 100)
y = x**2  # Distribución teórica para un ejemplo de desigualdad

# Calcular el índice de Gini como el área entre la diagonal y la curva de Lorenz
AUC_Lorenz = np.trapz(y, x)  # Área bajo la curva de Lorenz
AUC_total = 0.5  # Área bajo la línea de igualdad (triángulo de base 1 y altura 1)
gini = (AUC_total - AUC_Lorenz) / AUC_total  # Índice de Gini

# Crear la figura y el gráfico
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, label="Curva de Lorenz", color="blue", linewidth=2)
ax.plot(x, x, label="Igualdad perfecta", color="black", linestyle="dashed")

# Rellenar la zona entre la curva de Lorenz y la línea de igualdad
ax.fill_between(x, y, x, color="lightblue", alpha=0.5, label="Área de Gini")

# Etiquetas y título
ax.set_xlabel("Porcentaje acumulado de la población")
ax.set_ylabel("Porcentaje acumulado de la renta")
ax.set_title(f"Curva de Lorenz e Índice de Gini: {gini:.2f}")
ax.legend()
ax.grid(True)

# Mostrar el gráfico
plt.show()
