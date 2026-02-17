# verlet.py
import numpy as np


def integrate(t, a, dt, x0, v0):
    """
    Implements Velocity Verlet.
    """
    n = len(t)
    x = np.zeros(n)
    v = np.zeros(n)
    x[0], v[0] = x0, v0

    for i in range(n - 1):
        x[i + 1] = x[i] + v[i] * dt + 0.5 * a[i] * dt ** 2
        v[i + 1] = v[i] + 0.5 * (a[i] + a[i + 1]) * dt
    return x