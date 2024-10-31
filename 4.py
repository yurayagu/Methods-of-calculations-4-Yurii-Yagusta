import math
import pandas as pd
import matplotlib.pyplot as plt


def get_function(default_func_description, default_func):
    print(f"Default integration function: {default_func_description}")
    use_default = input("Do you want to continue with this function? (Enter 1 for yes, 2 for no): ").strip()
    if use_default == "1":
        return default_func
    else:
        user_input = input("f(x) = ")
        return lambda x: eval(user_input, {**vars(math), "x": x})


def rectangle_methods(f, a, b, n):
    h = (b - a) / n
    left_s = sum(f(a + i * h) for i in range(n)) * h
    right_s = sum(f(a + (i + 1) * h) for i in range(n)) * h
    mid_s = sum(f(a + (i + 0.5) * h) for i in range(n)) * h
    return {"Left Rectangle": left_s, "Right Rectangle": right_s, "Midpoint Rectangle": mid_s}


def simpsons_method(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    h = (b - a) / n
    s1 = sum(f(a + i * h) for i in range(1, n, 2))
    s2 = sum(f(a + i * h) for i in range(2, n, 2))
    return h / 3 * (f(a) + f(b) + 4 * s1 + 2 * s2)


def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    s = sum(f(a + i * h) for i in range(1, n))
    s += (f(a) + f(b)) / 2
    return s * h


def generate_xy_table(f, a, b, n):
    h = (b - a) / n
    data = {
        "i": range(n + 1),
        "x_i": [round(a + i * h, 4) for i in range(n + 1)],
        "y_i": [round(f(a + i * h), 4) for i in range(n + 1)]
    }
    return pd.DataFrame(data)


def generate_results(f, a, b, max_n, method):
    results = {"n": [], "Integral (S)": []}
    for n in range(2, max_n + 1, 2):
        if method == "Simpson's":
            results["Integral (S)"].append(round(simpsons_method(f, a, b, n), 4))
        elif method == "Trapezoidal":
            results["Integral (S)"].append(round(trapezoidal_method(f, a, b, n), 4))
        results["n"].append(n)
    return pd.DataFrame(results)


def main():
    print("Choose the integration method:")
    print("1. Rectangle Method")
    print("2. Simpson's Method")
    print("3. Trapezoidal Method")
    choice = input("Enter the number of the method you want to use: ").strip()

    if choice == "1":
        method_name = "Rectangle"
        f = get_function("f(x) = 1 / sqrt(0.2 * x + 1)", lambda x: 1 / math.sqrt(0.2 * x + 1))
        a = float(input("Enter a (e.g., 1.3): "))
        b = float(input("Enter b (e.g., 2.5): "))
        max_n = int(input("Enter the maximum number of division segments n (suggested: 10): ") or 10)

        xy_table_df = generate_xy_table(f, a, b, max_n)
        print("\nTable of x_i and y_i values:")
        print(xy_table_df.to_string(index=False))

        results_df = pd.DataFrame({
            "n": range(1, max_n + 1),
            "Left Rectangle": [round(rectangle_methods(f, a, b, n)["Left Rectangle"], 4) for n in range(1, max_n + 1)],
            "Right Rectangle": [round(rectangle_methods(f, a, b, n)["Right Rectangle"], 4) for n in range(1, max_n + 1)],
            "Midpoint Rectangle": [round(rectangle_methods(f, a, b, n)["Midpoint Rectangle"], 4) for n in range(1, max_n + 1)]
        })
        print("\nIntegration Results with different values of n:")
        print(results_df)

        # Побудова графіка для методу прямокутника
        plt.figure(figsize=(10, 5))
        plt.plot(results_df["n"], results_df["Left Rectangle"], marker="o", linestyle="-", label="Left Rectangle")
        plt.plot(results_df["n"], results_df["Right Rectangle"], marker="o", linestyle="-", label="Right Rectangle")
        plt.plot(results_df["n"], results_df["Midpoint Rectangle"], marker="o", linestyle="-", label="Midpoint Rectangle")
        plt.title("Integration results by Rectangle method for different n")
        plt.xlabel("Number of segments n")
        plt.ylabel("Integral (S)")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

    elif choice == "2":
        method_name = "Simpson's"
        f = get_function("f(x) = log10(x^2 + 0.8) / (x - 1)", lambda x: math.log10(x**2 + 0.8) / (x - 1))
        a = float(input("Enter a (e.g., 2.5): "))
        b = float(input("Enter b (e.g., 3.3): "))
        max_n = int(input("Enter the maximum number of division segments n (suggested: 8): ") or 8)

        xy_table_df = generate_xy_table(f, a, b, max_n)
        print("\nTable of x_i and y_i values:")
        print(xy_table_df.to_string(index=False))

        results_df = generate_results(f, a, b, max_n, method_name)
        print(f"\n{method_name} Method Integration Results:")
        print(results_df)

        # Побудова графіків за методом Сімпсона
        plt.figure(figsize=(10, 5))
        plt.plot(results_df["n"], results_df["Integral (S)"], marker="o", linestyle="-", label="Integral (S)")
        plt.title("Integration results by Simpson's method for different n")
        plt.xlabel("Number of segments n")
        plt.ylabel("Integral (S)")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

    elif choice == "3":
        method_name = "Trapezoidal"
        f = get_function("f(x) = 1 / sqrt(x^2 + 2)", lambda x: 1 / math.sqrt(x**2 + 2))
        a = float(input("Enter a (e.g., 0.5): "))
        b = float(input("Enter b (e.g., 1.3): "))
        max_n = int(input("Enter the maximum number of division segments n (suggested: 20): ") or 20)

        xy_table_df = generate_xy_table(f, a, b, max_n)
        print("\nTable of x_i and y_i values:")
        print(xy_table_df.to_string(index=False))

        results_df = generate_results(f, a, b, max_n, method_name)
        print(f"\n{method_name} Method Integration Results:")
        print(results_df)

        # Побудова графіка для методу трапецій
        plt.figure(figsize=(10, 5))
        plt.plot(xy_table_df["x_i"], xy_table_df["y_i"], marker="o", linestyle="-", label="Function f(x)")
        plt.title("Function values f(x) for Trapezoidal Method")
        plt.xlabel("x_i")
        plt.ylabel("y_i")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
