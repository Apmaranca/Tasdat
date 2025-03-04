import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
labels = [
    'Special\nPolicy',   # Purple
    'Commerce\nTax',     # Blue
    'Property\nTax',     # Green
    'Payroll\nTax',      # Yellow
    'Income\nTax'        # Orange
]

colors = [
    'purple',   # Special Policy
    'blue',     # Commerce Tax
    'green',    # Property Tax
    'yellow',   # Payroll Tax
    'orange'    # Income Tax
]

# Número total de pétalos
n_petals = 5

# Ángulo total del círculo (en radianes)
full_circle = 2 * np.pi

# Ángulo que cubre cada pétalo (con espacio entre ellos)
gap = np.deg2rad(5)  # Espacio entre pétalos (opcional)
petal_angle = (full_circle / n_petals) - gap

# Crear figura y eje polar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Radio interior y exterior (define grosor de los pétalos)
inner_radius = 0.4
outer_radius = 1.0

# Dibujar cada pétalo
for i in range(n_petals):
    start_angle = i * (full_circle / n_petals)  # inicio absoluto de cada sector
    end_angle = start_angle + petal_angle       # final absoluto

    # Definir los puntos del sector (dos líneas radiales y dos arcos)
    theta = np.linspace(start_angle, end_angle, 100)
    r_inner = np.full_like(theta, inner_radius)
    r_outer = np.full_like(theta, outer_radius)

    # Dibujar pétalo
    ax.fill_between(theta, r_inner, r_outer, color=colors[i], edgecolor='k', linewidth=1)

    # Posicionar etiqueta en el centro de cada pétalo
    label_angle = (start_angle + end_angle) / 2
    label_radius = (inner_radius + outer_radius) / 2
    ax.text(label_angle, label_radius, labels[i], ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Eliminar círculos concéntricos y marcas exteriores
ax.set_ylim(0, outer_radius)
ax.set_yticks([])
ax.set_xticks([])

# Añadir el texto central
plt.text(0, 0, "Tax System\nQuality Assessment", ha='center', va='center', fontsize=14, fontweight='bold', color='black')

# Ajustes finales
plt.title("", fontsize=14)  # Sin título superior
plt.show()

