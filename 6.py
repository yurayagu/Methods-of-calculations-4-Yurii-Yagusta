import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Toplevel, Frame


class NumericalMethods:
    def __init__(self, x0_a, y0_a, h_a, n_a, x0_b, y0_b, h_b, n_b):
        self.x0_a = x0_a
        self.y0_a = y0_a
        self.h_a = h_a
        self.n_a = n_a
        self.x0_b = x0_b
        self.y0_b = y0_b
        self.h_b = h_b
        self.n_b = n_b

    def f_euler(self, x, y):
        return x + np.sin(y / np.sqrt(3))

    def f_euler_cauchy(self, x, y):
        return x + np.cos(y / np.sqrt(1.25))

    def euler_method(self):
        x = [self.x0_a]
        y = [self.y0_a]
        for i in range(self.n_a):
            x_next = x[-1] + self.h_a
            y_next = y[-1] + self.h_a * self.f_euler(x[-1], y[-1])
            x.append(x_next)
            y.append(y_next)
        return x, y

    def euler_cauchy_method(self):
        x = [self.x0_b]
        y = [self.y0_b]
        for i in range(self.n_b):
            x_next = x[-1] + self.h_b
            y_predict = y[-1] + self.h_b * self.f_euler_cauchy(x[-1], y[-1])
            y_next = y[-1] + self.h_b / 2 * (self.f_euler_cauchy(x[-1], y[-1]) + self.f_euler_cauchy(x_next, y_predict))
            x.append(x_next)
            y.append(y_next)
        return x, y


class GraphPlotter:
    def __init__(self, x_euler, y_euler, x_euler_cauchy, y_euler_cauchy):
        self.x_euler = x_euler
        self.y_euler = y_euler
        self.x_euler_cauchy = x_euler_cauchy
        self.y_euler_cauchy = y_euler_cauchy

    def show_graphs(self):
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.plot(self.x_euler, self.y_euler, marker='o', label="Метод Ейлера", color='green')
        plt.title("Метод Ейлера")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(self.x_euler_cauchy, self.y_euler_cauchy, marker='s', label="Метод Ейлера-Коші", color="red")
        plt.title("Метод Ейлера-Коші")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.legend()

        plt.tight_layout()
        plt.show()


class TableViewer:
    def __init__(self, root, method_name, x_data, y_data):
        self.root = root
        self.method_name = method_name
        self.x_data = x_data
        self.y_data = y_data

    def show_table(self):
        table_page = Toplevel(self.root)
        table_page.title(f"Результати: {self.method_name}")
        table_page.geometry("500x400")

        Label(table_page, text=f"{self.method_name}", font=("Arial", 16, "bold")).pack(pady=10)
        table_text = "\n".join([f"{i:2d} | {xi:6.4f} | {yi:6.4f}" for i, (xi, yi) in enumerate(zip(self.x_data,
                                                                                                   self.y_data))])
        Label(table_page, text="i  |   xi   |   yi", font=("Courier", 14, "bold")).pack()
        Label(table_page, text=table_text, font=("Courier", 12), justify="left").pack(pady=10)
        Button(table_page, text="Закрити", command=table_page.destroy, font=("Arial", 12)).pack(pady=10)


class Application:
    def __init__(self, root, x0_a, y0_a, h_a, n_a, x0_b, y0_b, h_b, n_b):
        self.root = root
        self.numerical_methods = NumericalMethods(x0_a, y0_a, h_a, n_a, x0_b, y0_b, h_b, n_b)
        self.graph_plotter = None
        self.table_viewer = None
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Чисельне розв'язання диференціальних рівнянь")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        (Label(self.root, text="Чисельне розв'язання диференціальних рівнянь", font=("Arial", 18, "bold"),
               bg="#f0f0f0").pack(pady=20))
        (Label(self.root, text="Метод Ейлера: x0 = 1.1, y0 = 1.5, h = 0.1, n = 10", font=("Arial", 14),
               bg="#f0f0f0").pack(pady=10))
        (Label(self.root, text="Метод Ейлера-Коші: x0 = 0.4, y0 = 0.8, h = 0.1, n = 10", font=("Arial", 14),
               bg="#f0f0f0").pack(pady=10))

        button_frame = Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        Button(button_frame, text="Показати таблицю Ейлера", command=self.show_euler_table, font=("Arial", 14),
               width=30).pack(pady=10)
        Button(button_frame, text="Показати таблицю Ейлера-Коші", command=self.show_euler_cauchy_table,
               font=("Arial", 14), width=30).pack(pady=10)
        Button(button_frame, text="Показати графіки", command=self.show_graphs, font=("Arial", 14),
               width=30).pack(pady=10)

    def show_euler_table(self):
        x_euler, y_euler = self.numerical_methods.euler_method()
        self.table_viewer = TableViewer(self.root, "Метод Ейлера", x_euler, y_euler)
        self.table_viewer.show_table()

    def show_euler_cauchy_table(self):
        x_euler_cauchy, y_euler_cauchy = self.numerical_methods.euler_cauchy_method()
        self.table_viewer = TableViewer(self.root, "Метод Ейлера-Коші", x_euler_cauchy, y_euler_cauchy)
        self.table_viewer.show_table()

    def show_graphs(self):
        x_euler, y_euler = self.numerical_methods.euler_method()
        x_euler_cauchy, y_euler_cauchy = self.numerical_methods.euler_cauchy_method()
        self.graph_plotter = GraphPlotter(x_euler, y_euler, x_euler_cauchy, y_euler_cauchy)
        self.graph_plotter.show_graphs()


def main():
    x0_a, y0_a, h_a, n_a = 1.1, 1.5, 0.1, 10
    x0_b, y0_b, h_b, n_b = 0.4, 0.8, 0.1, 10

    root = Tk()
    app = Application(root, x0_a, y0_a, h_a, n_a, x0_b, y0_b, h_b, n_b)
    root.mainloop()


if __name__ == "__main__":
    main()
