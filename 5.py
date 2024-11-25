import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve, oo, lambdify


def main():
    x = symbols('x')

    equation = 3 * x**4 - x**3 + 10 * x**2 - 5 * x - 3
    print("Використовується функція: f(x) = 3x^4 - x^3 + 10x^2 - 5x - 3")

    derivative = diff(equation, x)
    print("\nПохідна функції: f'(x) =", derivative)

    derivative_roots = solve(derivative, x)
    real_derivative_roots = [r.evalf() for r in derivative_roots if r.is_real]
    print("\nКорені похідної функції (тільки дійсні):")
    for i, root in enumerate(real_derivative_roots, 1):
        print(f"x{i} ≈ {root:.6f}")

    critical_points = sorted(real_derivative_roots)
    intervals = [(-oo, critical_points[0])] + \
                [(critical_points[i], critical_points[i + 1]) for i in range(len(critical_points) - 1)] + \
                [(critical_points[-1], oo)]

    print("\nПроміжки знаків похідної функції:")
    for i, interval in enumerate(intervals, 1):
        print(f"Проміжок {i}: {interval}")

    def newton_method(eq, der, x0, max_iter=6):
        f = lambdify(x, eq)
        f_prime = lambdify(x, der)
        xn = x0
        steps = []
        for i in range(max_iter):
            fxn = f(xn)
            fpxn = f_prime(xn)
            if fpxn == 0:
                print("Помилка: Похідна дорівнює нулю.")
                break
            xn_next = xn - fxn / fpxn
            delta = abs(xn_next - xn) if i > 0 else None
            steps.append((i, xn, fxn, fpxn, delta))
            xn = xn_next
        return xn, steps

    def bisection_method(eq, a, b, eps=1e-7, max_iter=14):
        f = lambdify(x, eq)
        steps = []
        for i in range(max_iter):
            c = (a + b) / 2
            fc = f(c)
            steps.append((i, a, b, c, fc, abs(b - a)))
            if abs(fc) < eps:
                break
            if f(a) * fc < 0:
                b = c
            else:
                a = c
        return c, steps

    x1_initial = -0.75
    x1, newton_steps = newton_method(equation, derivative, x1_initial)

    print("\nМетод Ньютона:")
    print(f"{'n':<3}{'xn':<12}{'f(xn)':<12}{'f`(xn)':<12}{'|xn+1 - xn|':<12}")
    for step in newton_steps:
        delta = '-' if step[4] is None else f"{step[4]:.8f}"  # Прочерк для першої ітерації
        print(f"{step[0]:<3}{step[1]:<12.6f}{step[2]:<12.6f}{step[3]:<12.6f}{delta:<12}")

    a, b = 0.25, 1.25
    x2, bisection_steps = bisection_method(equation, a, b)

    print("\nМетод бісекції:")
    print(f"{'n':<3}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}{'|b - a|':<12}")
    for step in bisection_steps:
        print(f"{step[0]:<3}{step[1]:<12.6f}{step[2]:<12.6f}{step[3]:<12.6f}{step[4]:<12.6f}{step[5]:<12.6f}")

    print("\nУточнені корені:")
    print(f"x1 ≈ {x1:.6f}")
    print(f"x2 ≈ {x2:.6f}")

    f_lambdified = lambdify(x, equation)
    f_prime_lambdified = lambdify(x, derivative)
    x_vals = np.linspace(-2, 2, 1000)
    y_vals = f_lambdified(x_vals)
    y_prime_vals = f_prime_lambdified(x_vals)

    plt.figure(figsize=(12, 7))
    plt.plot(x_vals, y_vals, label="f(x)", color="red", linestyle='dashed', linewidth=2)
    plt.plot(x_vals, y_prime_vals, label="f'(x)", linestyle='dashed', color="green", linewidth=2)
    plt.axhline(0, color='black', linewidth=1.2, linestyle='--', label="Ox")
    plt.axvline(0, color='black', linewidth=1.2, linestyle='--', label="Oy")
    plt.title("Графік функції f(x) та її похідної", fontsize=14)
    plt.legend()
    plt.grid(color='gray', linestyle=':', linewidth=0.5)
    plt.show()


if __name__ == "__main__":
    main()
