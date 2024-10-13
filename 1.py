import tkinter as tk
from tkinter import messagebox
import math


# Завдання 1: Точність наближень
def absolute_error(real_value, approx_value):
    return abs(real_value - approx_value)


def relative_error(real_value, approx_value):
    return absolute_error(real_value, approx_value) / real_value


def task1():
    try:
        n1 = float(entry_n1.get())
        x1 = float(entry_x1.get())
        n2 = float(entry_n2.get())
        N2 = float(entry_N2.get())
        x2 = float(entry_x2.get())

        sqrt_n1 = math.sqrt(n1)
        exact_ratio = n2 / N2

        rel_error1 = relative_error(sqrt_n1, x1)
        rel_error2 = relative_error(exact_ratio, x2)

        if rel_error1 < rel_error2:
            result_task1.set(f"Наближення до sqrt({n1}) точніше: відносна похибка = {rel_error1:.4f}")
        else:
            result_task1.set(f"Наближення до {n2}/{N2} точніше: відносна похибка = {rel_error2:.4f}")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


def round_narrow(x, delta):
    return round(x, 2) if delta < 0.05 else round(x, 1)


def round_broad(x, delta_percent):
    delta = delta_percent / 100
    return round(x, 2) if delta < 0.05 else round(x, 1)


def task2():
    try:
        x = float(entry_x.get())
        rounding_choice = rounding_mode.get()

        if rounding_choice == 'narrow':
            delta = float(entry_delta.get())
            x_narrow = round_narrow(x, delta)
            result_task2.set(f"Округлене число (вузьке) = {x_narrow}")
        elif rounding_choice == 'broad':
            delta_percent = float(entry_delta_percent.get())
            x_broad = round_broad(x, delta_percent)
            result_task2.set(f"Округлене число (широке) = {x_broad}")
        else:
            messagebox.showerror("Помилка", "Оберіть режим округлення.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


def calculate_delta_narrow(x):
    try:
        decimal_places = len(str(x).split(".")[1]) if "." in str(x) else 0
        last_digit_value = 10 ** (-decimal_places)
        return last_digit_value / 2
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка обчислення вузької похибки: {str(e)}")
        return None


def calculate_delta_broad(x):
    try:
        decimal_places = len(str(x).split(".")[1]) if "." in str(x) else 0
        last_digit_value = 10 ** (-decimal_places)
        return last_digit_value
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка обчислення широкої похибки: {str(e)}")
        return None


def task3():
    try:
        x = float(entry_x_task3.get())
        choice = error_mode.get()

        if choice == 'narrow':
            delta_narrow = calculate_delta_narrow(x)
            if delta_narrow is not None:
                relative_error = delta_narrow / x
                result_task3.set(f"Абсолютна похибка (вузьке) = {delta_narrow:.4f}, Відносна похибка = {relative_error * 100:.4f}%")
            else:
                result_task3.set("Не вдалося обчислити похибку.")
        elif choice == 'broad':
            delta_broad = calculate_delta_broad(x)
            if delta_broad is not None:
                relative_error = delta_broad / x
                result_task3.set(f"Абсолютна похибка (широке) = {delta_broad:.4f}, Відносна похибка = {relative_error * 100:.4f}%")
            else:
                result_task3.set("Не вдалося обчислити похибку.")
        else:
            messagebox.showerror("Помилка", "Оберіть тип похибки.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


def main():
    global entry_n1, entry_x1, entry_n2, entry_N2, entry_x2
    global entry_x, rounding_mode, entry_delta, entry_delta_percent
    global entry_x_task3, error_mode
    global result_task1, result_task2, result_task3

    root = tk.Tk()
    root.title("Три завдання: Точність, Округлення та Похибки")
    root.geometry("400x500")

    tk.Label(root, text="Завдання 1: Точність наближень", font=("Arial", 10, "bold")).pack(pady=5)

    tk.Label(root, text="Число під коренем (n1):").pack()
    entry_n1 = tk.Entry(root)
    entry_n1.pack()

    tk.Label(root, text="Наближення sqrt(n1):").pack()
    entry_x1 = tk.Entry(root)
    entry_x1.pack()

    tk.Label(root, text="Чисельник дробу (n2):").pack()
    entry_n2 = tk.Entry(root)
    entry_n2.pack()

    tk.Label(root, text="Знаменник дробу (N2):").pack()
    entry_N2 = tk.Entry(root)
    entry_N2.pack()

    tk.Label(root, text="Наближення n2/N2:").pack()
    entry_x2 = tk.Entry(root)
    entry_x2.pack()

    result_task1 = tk.StringVar()
    tk.Button(root, text="Виконати завдання 1", command=task1).pack(pady=5)
    tk.Label(root, textvariable=result_task1).pack(pady=5)

    tk.Label(root, text="Завдання 2: Округлення числа", font=("Arial", 10, "bold")).pack(pady=5)

    tk.Label(root, text="Число (x):").pack()
    entry_x = tk.Entry(root)
    entry_x.pack()

    rounding_mode = tk.StringVar(value='narrow')
    tk.Radiobutton(root, text="Вузьке", variable=rounding_mode, value='narrow').pack()
    tk.Radiobutton(root, text="Широке", variable=rounding_mode, value='broad').pack()

    tk.Label(root, text="Абсолютна похибка (delta):").pack()
    entry_delta = tk.Entry(root)
    entry_delta.pack()

    tk.Label(root, text="Відсоткова похибка (delta%):").pack()
    entry_delta_percent = tk.Entry(root)
    entry_delta_percent.pack()

    result_task2 = tk.StringVar()
    tk.Button(root, text="Виконати завдання 2", command=task2).pack(pady=5)
    tk.Label(root, textvariable=result_task2).pack(pady=5)

    tk.Label(root, text="Завдання 3: Обчислення похибок", font=("Arial", 10, "bold")).pack(pady=5)

    tk.Label(root, text="Число (x):").pack()
    entry_x_task3 = tk.Entry(root)
    entry_x_task3.pack()

    error_mode = tk.StringVar(value='narrow')
    tk.Radiobutton(root, text="Вузьке", variable=error_mode, value='narrow').pack()
    tk.Radiobutton(root, text="Широке", variable=error_mode, value='broad').pack()

    result_task3 = tk.StringVar()
    tk.Button(root, text="Виконати завдання 3", command=task3).pack(pady=5)
    tk.Label(root, textvariable=result_task3).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
