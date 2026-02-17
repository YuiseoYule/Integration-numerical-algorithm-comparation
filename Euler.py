# Euler.py
import numpy as np


def integrate(t, a, dt, x0, v0):
    """
    Implements Forward Euler Integration.
    x[i+1] = x[i] + v[i] * dt
    v[i+1] = v[i] + a[i] * dt
    """
    n = len(t)
    x = np.zeros(n)
    v = np.zeros(n)
    x[0], v[0] = x0, v0

    for i in range(n - 1):
        v[i + 1] = v[i] + a[i] * dt
        x[i + 1] = x[i] + v[i] * dt
    return x