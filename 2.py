import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def input_points(root):
    # Введення кількості точок
    tk.Label(root, text="Enter the number of known points:").pack()
    entry_n = tk.Entry(root)
    entry_n.pack()

    def enter_n():
        n = int(entry_n.get())
        entry_n.pack_forget()

        # Введення значень X
        tk.Label(root, text="Enter values for X (known points):").pack()
        entries_x = [tk.Entry(root) for _ in range(n)]
        for entry in entries_x:
            entry.pack()

        # Введення значень Y
        tk.Label(root, text="Enter values for Y (known points):").pack()
        entries_y = [tk.Entry(root) for _ in range(n)]
        for entry in entries_y:
            entry.pack()

        def submit_values():
            XX = [float(entry.get()) for entry in entries_x]
            YY = [float(entry.get()) for entry in entries_y]

            # Виведення таблиці значень
            table = "\nTable of values of a function:\n"
            table += "X: " + "".join([f"{x:7.3f}|" for x in XX]) + "\n"
            table += "Y: " + "".join([f"{y:7.3f}|" for y in YY]) + "\n"
            messagebox.showinfo("Values Table", table)

            # Обчислення інтерполяційного багаточлена
            L_simplified = lagrange_interpolation(XX, YY)

            # Виведення інтерполяційного багаточлена
            result = f"The interpolation polynomial L(x) is:\n{L_simplified}\n"
            messagebox.showinfo("Lagrange Polynomial", result)

            # Переходження до другого вікна
            interpolate_points(XX, YY, L_simplified)

        tk.Button(root, text="Submit Values", command=submit_values).pack()

    tk.Button(root, text="Submit", command=enter_n).pack()


def lagrange_interpolation(XX, YY):
    x = sp.Symbol('x')
    n = len(XX)
    L = 0
    for i in range(n):
        term = YY[i]
        for j in range(n):
            if i != j:
                term *= (x - XX[j]) / (XX[i] - XX[j])
        L += term
    return sp.simplify(L)


def interpolate_points(XX, YY, L_simplified):
    # Створення вікна для введення точок інтерполяції
    interpolation_window = tk.Toplevel()
    interpolation_window.title("Interpolate Points")

    tk.Label(interpolation_window, text="Enter the number of points to interpolate:").pack()
    entry_m = tk.Entry(interpolation_window)
    entry_m.pack()

    def enter_m():
        m = int(entry_m.get())
        entry_m.pack_forget()

        # Введення значень для інтерполяції
        labels_interpolation = []
        entries_interpolation = []

        for i in range(m):
            label = tk.Label(interpolation_window, text=f"Enter value X[{i}] to interpolate:")
            label.pack()
            labels_interpolation.append(label)
            entry = tk.Entry(interpolation_window)
            entry.pack()
            entries_interpolation.append(entry)

        def submit_interpolation():
            interpolation_results = ""
            for entry in entries_interpolation:
                r = float(entry.get())
                y_value = L_simplified.subs(sp.Symbol('x'), r)
                interpolation_results += f"For X = {r:.1f}, Y = {y_value:.3f}\n"

            messagebox.showinfo("Interpolation Results", interpolation_results)

            # Побудова графіка
            plot_graph(XX, YY, L_simplified)

        tk.Button(interpolation_window, text="Submit Interpolation Values", command=submit_interpolation).pack()

    tk.Button(interpolation_window, text="Submit", command=enter_m).pack()


def plot_graph(XX, YY, L_simplified):
    L_func = sp.lambdify(sp.Symbol('x'), L_simplified, 'numpy')
    x_vals = np.linspace(min(XX) - 1, max(XX) + 1, 500)
    y_vals = L_func(x_vals)

    # Побудова графіка
    plt.plot(x_vals, y_vals, label='Lagrange Polynomial', color='orange')
    plt.scatter(XX, YY, color='blue', label='Given Points')

    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')

    plt.title('Lagrange Interpolation Polynomial')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    root = tk.Tk()
    root.title("Lagrange Interpolation")
    input_points(root)
    root.mainloop()


if __name__ == "__main__":
    main()
