import numpy as np
import matplotlib.pyplot as plt

A = 1.0
f = 1.0
phi = 0.0
t_start = 0.0
t_end = 2.0
dt = 0.001

t_continuous = np.arange(t_start, t_end, dt)
x_continuous = A * np.cos(2 * np.pi * f * t_continuous + phi)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t_continuous, x_continuous, 'b-', linewidth=1.5)
plt.title(r'Continuous Signal: Cosine Wave $x(t) = \cos(2\pi t)$', fontsize=12)
plt.xlabel('Time t (s)', fontsize=10)
plt.ylabel('Amplitude x(t)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-1.2, 1.2)

n_start = -5
n_end = 5
n_discrete = np.arange(n_start, n_end + 1)

x_discrete = np.zeros_like(n_discrete)
x_discrete[n_discrete == 0] = 1.0

plt.subplot(1, 2, 2)

plt.stem(n_discrete, x_discrete, 'r-', basefmt='k-')
plt.title(r'Discrete Signal: Unit Impulse $\delta[n]$', fontsize=12)
plt.xlabel('Discrete Time n', fontsize=10)
plt.ylabel('Amplitude x[n]', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-0.2, 1.2)
plt.xticks(n_discrete)

plt.tight_layout()
plt.show()