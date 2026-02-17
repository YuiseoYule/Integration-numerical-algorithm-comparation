# Integration-numerical-algorithm-comparation
# Kinematic Integrator Benchmark

A modular Python framework for simulating and benchmarking numerical integration algorithms in kinematic systems. This project solves the Initial Value Problem (IVP) for second-order differential equations ($\ddot{x} = a(t)$), comparing the stability and accuracy of symplectic and non-symplectic integrators against ground-truth data.

## 📂 Project Structure

The project follows a modular design pattern to ensure extensibility and separation of concerns:

\`\`\`bash
├── data.csv          # Input time-series data (Time, Acceleration, Displacement)
├── euler.py          # Forward Euler integration module (Order 1)
├── rk2.py            # Runge-Kutta 2nd Order / Heun's Method module (Order 2)
├── rk4.py            # Runge-Kutta 4th Order module (Order 4)
├── verlet.py         # Velocity Verlet symplectic integrator module (Order 2)
└── evaluator.py      # Main execution script for benchmarking and visualization
\`\`\`

## 🚀 Algorithms Implemented

This repository implements four distinct numerical methods to reconstruct displacement ($x$) from discrete acceleration ($a$) data:

* **Forward Euler (`euler.py`):** First-order estimation. Fast but suffers from significant global truncation error ($O(\Delta t)$).
* **Heun's Method / RK2 (`rk2.py`):** A predictor-corrector approach that improves accuracy to $O(\Delta t^2)$ by averaging slopes.
* **Runge-Kutta 4 (`rk4.py`):** The standard high-fidelity solver for non-stiff systems ($O(\Delta t^4)$). It samples four derivatives per step to minimize error.
* **Velocity Verlet (`verlet.py`):** A symplectic integrator commonly used in molecular dynamics. It offers superior energy conservation and long-term stability compared to non-symplectic methods of the same order.

## 📊 Usage

1.  **Prepare Data:** Ensure `data.csv` contains `time`, `acceleration`, and `displacement` (for validation) columns.
2.  **Run Simulation:** Execute the main evaluator script.
    \`\`\`bash
    python evaluator.py
    \`\`\`
3.  **Output:** The script generates a comparative plot (`comparison.png`) and prints an error metrics table (RMSE/MAE) to the console.

## 📈 Results

*Example output based on synthetic harmonic motion:*

| Algorithm | RMSE (m) | MAE (m) |
| :--- | :--- | :--- |
| **Euler** | 0.0256 | 0.0212 |
| **RK2** | 2.0e-4 | 1.7e-4 |
| **RK4** | 1.9e-4 | 1.6e-4 |
| **Verlet** | 2.0e-4 | 1.7e-4 |
