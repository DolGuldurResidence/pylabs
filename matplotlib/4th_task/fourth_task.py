import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def sine_wave(amplitude, frequency, t):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Initial parameters
t = np.linspace(0, 1, 1000)
initial_amplitude1 = 1
initial_frequency1 = 1
initial_amplitude2 = 1
initial_frequency2 = 1

fig, (ax1, ax2, ax_sum) = plt.subplots(3, 1, figsize=(10, 8))

plt.subplots_adjust(left=0.1, bottom=0.25)

line1, = ax1.plot(t, sine_wave(initial_amplitude1, initial_frequency1, t), lw=2)
line2, = ax2.plot(t, sine_wave(initial_amplitude2, initial_frequency2, t), lw=2)
line_sum, = ax_sum.plot(t, sine_wave(initial_amplitude1, initial_frequency1, t) + sine_wave(initial_amplitude2, initial_frequency2, t), lw=2)

ax1.set_title('Sine Wave 1')
ax2.set_title('Sine Wave 2')
ax_sum.set_title('Sum of Sine Waves')
for ax in [ax1, ax2, ax_sum]:
    ax.set_xlim(0, 1)
    ax.set_ylim(-5, 5)

ax_amp1 = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_freq1 = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_amp2 = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_freq2 = plt.axes([0.1, 0, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_amp1 = Slider(ax_amp1, 'Amp 1', 0.1, 2.0, valinit=initial_amplitude1)
slider_freq1 = Slider(ax_freq1, 'Freq 1', 0.1, 5.0, valinit=initial_frequency1)
slider_amp2 = Slider(ax_amp2, 'Amp 2', 0.1, 2.0, valinit=initial_amplitude2)
slider_freq2 = Slider(ax_freq2, 'Freq 2', 0.1, 5.0, valinit=initial_frequency2)

def update(val):
    amp1 = slider_amp1.val
    freq1 = slider_freq1.val
    amp2 = slider_amp2.val
    freq2 = slider_freq2.val
    y1 = sine_wave(amp1, freq1, t)
    y2 = sine_wave(amp2, freq2, t)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line_sum.set_ydata(y1 + y2)
    fig.canvas.draw_idle()

slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

plt.show()