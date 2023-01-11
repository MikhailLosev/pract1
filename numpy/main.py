import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

def main():
    def f(x):
        return np.log(5 * x ** 3) * np.sin(6 * x)

    def diff_f(x):
        return 6 * np.cos(6 * x) * np.log(5 * x ** 3) + (3 * np.sin(6 * x) / x)

    def intr(x):
        return math.sqrt(1 + (6 * np.cos(6 * x) * np.log(5 * x ** 3) + (3 * np.sin(6 * x) / x)) ** 2)
    x = np.arange(0, 5, 0.01)
    func = np.log(5*x**3)*np.sin(6*x)
    main_func = plt.plot(x,func)
    f_min = 1000
    f_max = -1000

    for i in x:
        if f(i) > f_max:
            f_max = f(i)
            x_max = i
        if f(i) < f_min:
            f_min = f(i)
            x_min = i

    max_dot = plt.plot(x_max, f_max, 'o', color = 'b')
    min_dot = plt.plot(x_min, f_min, 'o', color = 'r')

    x0 = 1
    y0 = f(x0)
    M = plt.plot(x0, y0, 'o', color = 'green')
    diff_y0 = diff_f(x0)

    normal = y0 - (1/diff_y0)*(x - x0)
    tangent = y0 + diff_y0 * (x - x0)

    plt.plot(x,normal)
    plt.plot(x,tangent)
    plt.show()

    diff_y = 6*np.cos(6*x)*np.log(5*x**3)+(3*np.sin(6*x)/x)
    plt.plot(x,diff_y)
    plt.show()

    diff_2_y = 3*(-np.sin(6*x)/x**2 - 12*np.log(5*x**3)*np.sin(6*x) + 12*np.cos(6*x)/x)
    plt.plot(x, diff_2_y)
    plt.show()

    for i in np.arange (0., 5.5, 0.5):
        x0 = i
        y0 = f(x0)
        diff_y0 = diff_f(x0)
        tangent = y0 + diff_y0 * (x - x0)
        plt.plot(x, tangent,color = 'y')
    plt.plot(x,func)

    plt.show()

    v, err = integrate.quad(intr, 0, 5)
    print(v)

if __name__ == "__main__":
    main()