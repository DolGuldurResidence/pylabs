import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmn
from scipy.special import eval_legendre
plt.style.use('seaborn-v0_8-notebook')

x = np.linspace(-1, 1, 400)

fig, ax = plt.subplots()
ax.set_title('Полиномы Лежандра')

for n in range(1, 8):
    Pn = eval_legendre(n, x)
    ax.plot(x, Pn, label=f'n = {n}')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.35, 1))

plt.show()