import tkinter as tk
from tkinter import messagebox
import math


# Абсолютна похибка
def absolute_error(real_value, approx_value):
    return abs(real_value - approx_value)


# Завдання 1: визначення точнішого наближення
def task1():
    try:
        n1 = float(entry_n1.get())
        x1 = float(entry_x1.get())
        n2 = float(entry_n2.get())
        N2 = float(entry_N2.get())
        x2 = float(entry_x2.get())

        sqrt_n1 = math.sqrt(n1)
        exact_ratio = n2 / N2

        error1 = absolute_error(sqrt_n1, x1)
        error2 = absolute_error(exact_ratio, x2)

        if error1 < error2:
            result_task1.set(f"Наближення до sqrt({n1}) точніше: абсолютна похибка = {error1:.4f}")
        else:
            result_task1.set(f"Наближення до {n2}/{N2} точніше: абсолютна похибка = {error2:.4f}")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


# Вузьке розуміння (округлення)
def round_narrow(x, delta):
    return round(x, 2)


# Широке розуміння (округлення)
def round_broad(x, delta_percent):
    delta = delta_percent / 100
    x_rounded = round(x * (1 - delta), 2)
    return x_rounded


# Завдання 2: округлення числа
def task2():
    try:
        x = float(entry_x.get())
        rounding_choice = rounding_mode.get()

        if rounding_choice == 'narrow':
            delta = float(entry_delta.get())
            x_narrow = round_narrow(x, delta)
            result_task2.set(f"Округлене число (вузьке розуміння) = {x_narrow}")
        elif rounding_choice == 'broad':
            delta_percent = float(entry_delta_percent.get())
            x_broad = round_broad(x, delta_percent)
            result_task2.set(f"Округлене число (широке розуміння) = {x_broad}")
        else:
            messagebox.showerror("Помилка", "Оберіть режим округлення.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


# Абсолютна похибка (вузьке розуміння)
def calculate_delta_narrow(x):
    decimal_places = len(str(x).split(".")[1]) if "." in str(x) else 0
    last_digit_value = 10 ** (-decimal_places)
    return last_digit_value / 2


# Абсолютна похибка (широке розуміння)
def calculate_delta_broad(x):
    decimal_places = len(str(x).split(".")[1])
    last_digit_value = 10 ** (-decimal_places)
    return last_digit_value


# Завдання 3: обчислення похибок
def task3():
    try:
        x = float(entry_x_task3.get())
        choice = error_mode.get()

        if choice == 'narrow':
            delta_narrow = calculate_delta_narrow(x)
            relative_error = delta_narrow / x
            result_task3.set(f"Абсолютна похибка (вузьке розуміння) = {delta_narrow:.4f}, "
                             f"Відносна похибка = {relative_error * 100:.4f}%")
        elif choice == 'broad':
            delta_broad = calculate_delta_broad(x)
            relative_error = delta_broad / x
            result_task3.set(f"Абсолютна похибка (широке розуміння) = {delta_broad:.4f}, "
                             f"Відносна похибка = {relative_error * 100:.4f}%")
        else:
            messagebox.showerror("Помилка", "Оберіть тип похибки.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


# Створення вікна
root = tk.Tk()
root.title("Розрахунок похибок")
root.geometry("600x750")
root.configure(bg='#f0f0f0')

# Завдання 1: Точність наближень
tk.Label(root, text="Завдання 1: Точність наближень", font=("Arial", 14), bg='#f0f0f0').pack(pady=10)

frame_task1 = tk.Frame(root, bg='#f0f0f0')
frame_task1.pack()

tk.Label(frame_task1, text="Число під коренем (n1):", bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=5)
entry_n1 = tk.Entry(frame_task1)
entry_n1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_task1, text="Наближення sqrt(n1):", bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=5)
entry_x1 = tk.Entry(frame_task1)
entry_x1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_task1, text="Чисельник дробу (n2):", bg='#f0f0f0').grid(row=2, column=0, padx=10, pady=5)
entry_n2 = tk.Entry(frame_task1)
entry_n2.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_task1, text="Знаменник дробу (N2):", bg='#f0f0f0').grid(row=3, column=0, padx=10, pady=5)
entry_N2 = tk.Entry(frame_task1)
entry_N2.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame_task1, text="Наближення n2/N2:", bg='#f0f0f0').grid(row=4, column=0, padx=10, pady=5)
entry_x2 = tk.Entry(frame_task1)
entry_x2.grid(row=4, column=1, padx=10, pady=5)

result_task1 = tk.StringVar()
tk.Label(root, textvariable=result_task1, font=("Arial", 12), bg='#f0f0f0', fg='green').pack(pady=5)

tk.Button(root, text="Виконати завдання 1", command=task1, bg='lightblue').pack(pady=10)

# Завдання 2: Округлення числа
tk.Label(root, text="Завдання 2: Округлення числа", font=("Arial", 14), bg='#f0f0f0').pack(pady=10)

frame_task2 = tk.Frame(root, bg='#f0f0f0')
frame_task2.pack()

tk.Label(frame_task2, text="Число (x):", bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(frame_task2)
entry_x.grid(row=0, column=1, padx=10, pady=5)

rounding_mode = tk.StringVar(value='narrow')
tk.Radiobutton(frame_task2, text="Вузьке розуміння", variable=rounding_mode, value='narrow', bg='#f0f0f0').grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=5)
tk.Radiobutton(frame_task2, text="Широке розуміння", variable=rounding_mode, value='broad', bg='#f0f0f0').grid(row=1,
                                                                                                               column=1,
                                                                                                               padx=10,
                                                                                                               pady=5)

tk.Label(frame_task2, text="Абсолютна похибка (delta):", bg='#f0f0f0').grid(row=2, column=0, padx=10, pady=5)
entry_delta = tk.Entry(frame_task2)
entry_delta.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_task2, text="Відсоткова похибка (delta%):", bg='#f0f0f0').grid(row=3, column=0, padx=10, pady=5)
entry_delta_percent = tk.Entry(frame_task2)
entry_delta_percent.grid(row=3, column=1, padx=10, pady=5)

result_task2 = tk.StringVar()
tk.Label(root, textvariable=result_task2, font=("Arial", 12), bg='#f0f0f0', fg='green').pack(pady=5)

tk.Button(root, text="Виконати завдання 2", command=task2, bg='lightblue').pack(pady=10)

# Завдання 3: Похибки округлення
tk.Label(root, text="Завдання 3: Похибки округлення", font=("Arial", 14), bg='#f0f0f0').pack(pady=10)

frame_task3 = tk.Frame(root, bg='#f0f0f0')
frame_task3.pack()

tk.Label(frame_task3, text="Число (x):", bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=5)
entry_x_task3 = tk.Entry(frame_task3)
entry_x_task3.grid(row=0, column=1, padx=10, pady=5)

error_mode = tk.StringVar(value='narrow')
tk.Radiobutton(frame_task3, text="Вузьке розуміння", variable=error_mode, value='narrow', bg='#f0f0f0').grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=5)
tk.Radiobutton(frame_task3, text="Широке розуміння", variable=error_mode, value='broad', bg='#f0f0f0').grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

result_task3 = tk.StringVar()
tk.Label(root, textvariable=result_task3, font=("Arial", 12), bg='#f0f0f0', fg='green').pack(pady=5)

tk.Button(root, text="Виконати завдання 3", command=task3, bg='lightblue').pack(pady=10)

root.mainloop()
