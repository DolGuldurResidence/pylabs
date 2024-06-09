
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-notebook')

def lisago_figure(a, b, delta):
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(a*t + delta)
    y = np.sin(b*t)
    return x, y

fig, axs = plt.subplots(2, 2, figsize=(12, 12))

for ax, (a, b) in zip(axs.flat,[(3, 2),(3, 4),(5, 4),(5, 6)]):
    x, y = lisago_figure(a, b, 0)
    ax.plot(x, y)
    ax.set_title(f'lisago figure ({a}:{b})')
    ax.axis('equal')

plt.tight_layout()
plt.show()