# rk2.py
import numpy as np


def integrate(t, a, dt, x0, v0):
    """
    Implements RK2 (Heun's Method).
    """
    n = len(t)
    x = np.zeros(n)
    v = np.zeros(n)
    x[0], v[0] = x0, v0

    for i in range(n - 1):
        k1_v = a[i]
        k1_x = v[i]

        # Predictor (Euler step)
        v_pred = v[i] + k1_v * dt

        k2_v = a[i + 1]
        k2_x = v_pred

        # Corrector
        v[i + 1] = v[i] + 0.5 * (k1_v + k2_v) * dt
        x[i + 1] = x[i] + 0.5 * (k1_x + k2_x) * dt
    return x