import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Título de la aplicación
st.title('Casa de Chocolate 3D con Techo Dormer')

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dimensiones de la casa
altura_paredes = 2  # metros
ancho = 3           # metros
profundidad = 4     # metros
altura_techo = 1.5  # metros
altura_dormer = 1   # metros para el dormer

# Definición de los vértices de la casa
v = [
    # Pared frontal
    [0, 0, 0],
    [ancho, 0, 0],
    [ancho, 0, altura_paredes],
    [0, 0, altura_paredes],
    
    # Pared trasera
    [0, profundidad, 0],
    [ancho, profundidad, 0],
    [ancho, profundidad, altura_paredes],
    [0, profundidad, altura_paredes],
    
    # Pared izquierda
    [0, 0, 0],
    [0, profundidad, 0],
    [0, profundidad, altura_paredes],
    [0, 0, altura_paredes],
    
    # Pared derecha
    [ancho, 0, 0],
    [ancho, profundidad, 0],
    [ancho, profundidad, altura_paredes],
    [ancho, 0, altura_paredes],

    # Vértices del techo
    [0, 0, altura_paredes],
    [ancho / 2, 0, altura_paredes + altura_techo],  # Punto superior del techo
    [ancho, 0, altura_paredes],
    [0, profundidad, altura_paredes],
    [ancho / 2, profundidad, altura_paredes + altura_techo],  # Punto superior del dormer
    [ancho, profundidad, altura_paredes],
]

# Definición de las caras de la casa
caras = [
    [v[0], v[1], v[2], v[3]],  # Pared frontal
    [v[4], v[5], v[6], v[7]],  # Pared trasera
    [v[8], v[9], v[10], v[11]],  # Pared izquierda
    [v[12], v[13], v[14], v[15]],  # Pared derecha
    [v[16], v[17], v[18]],  # Techo frontal
    [v[19], v[20], v[21]],  # Techo trasero
    [v[18], v[17], v[20]],  # Lado izquierdo del dormer
    [v[18], v[20], v[21]],  # Lado derecho del dormer
]

# Añadir las caras a la visualización
ax.add_collection3d(Poly3DCollection(caras, facecolors='saddlebrown', linewidths=1, edgecolors='k', alpha=.25))

# Añadir la puerta
door_width = 0.5  # metros
door_height = 0.8  # metros
x_door = [1.25, 1.25, 1.75, 1.75]
y_door = [0, 0, 0, 0]
z_door = [0, door_height, door_height, 0]
ax.add_collection3d(Poly3DCollection([list(zip(x_door, y_door, z_door))], facecolors='peru', linewidths=1, edgecolors='k'))

# Añadir ventanas
window_width = 0.5  # metros
window_height = 0.5  # metros

# Ventana izquierda
x_window_left = [0.25, 0.25, 0.75, 0.75]
y_window_left = [0, 0, 0, 0]
z_window_left = [1.25, 1.75, 1.75, 1.25]
ax.add_collection3d(Poly3DCollection([list(zip(x_window_left, y_window_left, z_window_left))], facecolors='lightblue', linewidths=1, edgecolors='k'))

# Ventana derecha
x_window_right = [2.25, 2.25, 2.75, 2.75]
y_window_right = [0, 0, 0, 0]
z_window_right = [1.25, 1.75, 1.75, 1.25]
ax.add_collection3d(Poly3DCollection([list(zip(x_window_right, y_window_right, z_window_right))], facecolors='lightblue', linewidths=1, edgecolors='k'))

# Configuración del gráfico
ax.set_xlabel('Ancho (m)')
ax.set_ylabel('Profundidad (m)')
ax.set_zlabel('Altura (m)')
ax.set_title('Casa de Chocolate 3D con Techo Dormer')

# Añadir etiquetas de dimensiones
ax.text(1.5, -0.5, 1, 'Ancho = 3 m', color='black', fontsize=10)
ax.text(3.5, 2, 1, 'Profundidad = 4 m', color='black', fontsize=10)
ax.text(1.5, 0, 2, 'Altura = 2 m', color='black', fontsize=10)
ax.text(1.5, 0, 2.5, 'Techo = 1.5 m', color='black', fontsize=10)

# Mostrar el gráfico
st.pyplot(fig)
