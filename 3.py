import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_data_from_csv(file_path):
    data = pd.read_csv(file_path, delimiter='\t')
    X = data['x_i'].values
    Y = data['y_i'].values
    return X, Y


def display_table(X, Y):
    print("\nTable of values of a function:")
    print("\tX\t|\tY")
    print(" ---------------------------")
    for i in range(len(X)):
        print(f"\t{X[i]:.1f}\t|\t{Y[i]:.3f}")
    print()


def calculate_h(X):
    h = X[1] - X[0]
    print(f"Calculated h = {h:.2f}")
    return h


def calculate_deltas(Y):
    n = len(Y)
    deltas = [Y.copy()]

    for i in range(1, n):
        delta_i = np.zeros(n - i)
        for j in range(n - i):
            delta_i[j] = deltas[i - 1][j + 1] - deltas[i - 1][j]
        deltas.append(delta_i)

    print("\nDeltas table:")
    for i, delta in enumerate(deltas):
        print(f"Delta {i}: {delta}")

    return deltas


def calculate_q(xx, X, h):
    j = 0
    for i in range(len(X)):
        if X[i] < xx:
            j = i
        else:
            break

    q = (xx - X[j]) / h
    print(f"\nCalculated q for x = {xx:.2f} -> q = {q:.4f} (using X[{j}] = {X[j]:.2f})")
    return j


def calculate_derivatives(x, deltas, h, q, j):
    y1 = deltas[1][j] if j < len(deltas[1]) else 0
    y2 = deltas[2][j] if j < len(deltas[2]) else 0
    y3 = deltas[3][j] if j < len(deltas[3]) else 0
    y4 = deltas[4][j] if j < len(deltas[4]) else 0
    y5 = deltas[5][j] if j < len(deltas[5]) else 0

    G = (y1 + y2 * (2 * q - 1) / 2 + y3 * (3 * q**2 - 6 * q + 2) / 6 +
         y4 * (4 * q**3 - 18 * q**2 + 22 * q - 6) / 24 +
         y5 * (5 * q**4 - 40 * q**3 + 105 * q**2 - 100 * q + 24) / 120) / h

    L = (y2 + y3 * (q - 1) + y4 * (12 * q**2 - 36 * q + 22) / 24 +
         y5 * (20 * q**3 - 120 * q**2 + 210 * q - 100) / 120) / (h**2)

    return G, L


def plot_graph(X, Y, xx_values, G_values, L_values):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(X, Y, 'violet', marker='o', label="Y(x)")
    plt.title("Function Y(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(xx_values, G_values, 'orange', marker='o', label="Y'(x)")
    plt.plot(xx_values, L_values, 'lightblue', marker='o', label="Y''(x)")
    plt.title("Derivatives Y'(x) and Y''(x)")
    plt.xlabel("X")
    plt.ylabel("Derivatives")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    file_path = 'methods_lab3'
    X, Y = read_data_from_csv(file_path)
    display_table(X, Y)

    h = calculate_h(X)
    deltas = calculate_deltas(Y)

    m = int(input("\nEnter the number of values to check (xx): "))
    xx_values = np.zeros(m)
    G_values = np.zeros(m)
    L_values = np.zeros(m)

    for i in range(m):
        xx_values[i] = float(input(f"Enter value xx[{i}] = "))  # 3.35, 3.28

    for i, xx in enumerate(xx_values):
        j = calculate_q(xx, X, h)
        q = (xx - X[j]) / h
        G_values[i], L_values[i] = calculate_derivatives(X, deltas, h, q, j)

        print(f"For x = {xx:.2f}: Y' = {G_values[i]:.4f}, Y'' = {L_values[i]:.4f}")

    plot_graph(X, Y, xx_values, G_values, L_values)


if __name__ == "__main__":
    main()
