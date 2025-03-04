import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
labels = [
    'Property Tax', 
    'Commerce Tax', 
    'Income Tax', 
    'Payroll Tax', 
    'Special Policy'
]

colors = [
    'green',     # Property Tax
    'blue',      # Commerce Tax
    'orange',    # Income Tax
    'yellow',    # Payroll Tax
    'purple'     # Special Policy
]

# Número total de pétalos
n_petals = 5

# Ángulo total del círculo (en radianes)
full_circle = 2 * np.pi

# Ángulo que cubre cada pétalo
petal_angle = full_circle / n_petals

# Espacio (gap) entre pétalos (en radianes), por ejemplo 5 grados convertidos a radianes
gap = np.deg2rad(5)

# Ángulo efectivo para cada pétalo (descontando el gap)
effective_petal_angle = petal_angle - gap

# Crear figura y eje polar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Radio interior y exterior (para simular pétalos tipo "anillo")
inner_radius = 0.5
outer_radius = 1.0

# Dibujar cada pétalo
for i in range(n_petals):
    start_angle = i * petal_angle  # Ángulo de inicio para cada pétalo
    end_angle = start_angle + effective_petal_angle  # Ángulo de fin
    
    # Definir los ángulos y radios
    theta = np.linspace(start_angle, end_angle, 100)
    r_inner = np.full_like(theta, inner_radius)
    r_outer = np.full_like(theta, outer_radius)
    
    # Dibujar la franja (pétalo)
    ax.fill_between(theta, r_inner, r_outer, color=colors[i], edgecolor='k', linewidth=1)

    # Posicionar las etiquetas (un poco hacia afuera del borde)
    label_angle = (start_angle + end_angle) / 2
    label_radius = outer_radius + 0.1
    ax.text(label_angle, label_radius, labels[i], ha='center', va='center', fontsize=10, fontweight='bold')

# Ajustes finales del gráfico
ax.set_ylim(0, outer_radius + 0.2)
ax.set_yticks([])  # Oculta círculos concéntricos
ax.set_xticks([])  # Oculta marcas angulares

# Título
plt.title("Tax Distribution Wheel", va='bottom', fontsize=14)

# Mostrar
plt.show()
