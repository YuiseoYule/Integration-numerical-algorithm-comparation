# evaluator.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the modules (assuming they are in the same folder)
import Euler, RK2, RK4, Verlet


def calculate_errors(pred, truth):
    rmse = np.sqrt(np.mean((pred - truth) ** 2))
    mae = np.mean(np.abs(pred - truth))
    return rmse, mae


def main():
    # Load Data
    data = pd.read_csv('data.csv')
    t = data['time'].values
    a = data['acceleration'].values
    x_gt = data['displacement'].values  # Ground Truth

    dt = t[1] - t[0]
    x0 = x_gt[0]
    v0 = 0.0  # Assuming start from rest or known v0

    algorithms = {
        'Euler': Euler.integrate,
        'RK2': RK2.integrate,
        'RK4': RK4.integrate,
        'Verlet': Verlet.integrate
    }

    results = []

    plt.figure(figsize=(10, 6))
    plt.plot(t, x_gt, 'k-', label='Ground Truth', linewidth=2, alpha=0.7)

    for name, func in algorithms.items():
        x_pred = func(t, a, dt, x0, v0)
        rmse, mae = calculate_errors(x_pred, x_gt)
        results.append({'Algorithm': name, 'RMSE (m)': rmse, 'MAE (m)': mae})
        plt.plot(t, x_pred, '--', label=f'{name}')

    # Build Table
    results_df = pd.DataFrame(results)
    print("### Algorithm Performance Table")
    print(results_df)

    # Build Figure
    plt.title('Displacement Integration Comparison')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparison.png')
    plt.show()


if __name__ == "__main__":
    main()