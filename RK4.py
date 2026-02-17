# rk4.py
import numpy as np


def integrate(t, a, dt, x0, v0):
    """
    Implements RK4.
    Note: For discrete acceleration data, intermediate 'a' values
    are approximated by averaging.
    """
    n = len(t)
    x = np.zeros(n)
    v = np.zeros(n)
    x[0], v[0] = x0, v0

    for i in range(n - 1):
        # k1
        kv1 = a[i]
        kx1 = v[i]

        # k2 & k3 (midpoint approx for a)
        a_mid = 0.5 * (a[i] + a[i + 1])
        v_mid1 = v[i] + kv1 * dt * 0.5

        kv2 = a_mid
        kx2 = v_mid1

        v_mid2 = v[i] + kv2 * dt * 0.5
        kv3 = a_mid
        kx3 = v_mid2

        # k4
        v_end = v[i] + kv3 * dt
        kv4 = a[i + 1]
        kx4 = v_end

        v[i + 1] = v[i] + (dt / 6.0) * (kv1 + 2 * kv2 + 2 * kv3 + kv4)
        x[i + 1] = x[i] + (dt / 6.0) * (kx1 + 2 * kx2 + 2 * kx3 + kx4)
    return x