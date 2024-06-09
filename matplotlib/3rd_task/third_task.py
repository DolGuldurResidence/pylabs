import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(b):
    a = 1  # фиксированное значение для одной частоты
    x, y = np.sin(a*b*np.pi)*np.sin(b*2*np.pi*np.linspace(0, 1, 1000)), np.sin(a*b*np.pi)*np.cos(b*2*np.pi*np.linspace(0, 1, 1000))
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 120), init_func=init, interval=50, blit=True)
plt.axis('off')
plt.show()