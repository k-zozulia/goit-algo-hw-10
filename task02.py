import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2
N = 100000

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_curve = y_random < f(x_random)

area_monte_carlo = (b - a) * f(b) * np.sum(under_curve) / N

print(f"Метод Монте-Карло: площа під кривою = {area_monte_carlo}")

result_quad, error_quad = spi.quad(f, a, b)
print(f"Інтеграл за допомогою функції quad: {result_quad}, з помилкою: {error_quad}")

x = np.linspace(a, b, 400)
y = f(x)

plt.plot(x, y, 'r', linewidth=2)
plt.fill_between(x, y, color='gray', alpha=0.3)
plt.scatter(x_random, y_random, c=under_curve, cmap='coolwarm', s=1)
plt.title('Інтегрування методом Монте-Карло')
plt.grid(True)

plt.savefig("monte_carlo_plot.png")