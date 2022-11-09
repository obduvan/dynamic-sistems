from typing import List

import matplotlib.pyplot as plt
import numpy

from Figure import MyFunction
from export_to_matlab import export_two_arr


def bifurcation_a(func: MyFunction, x0, a0_max, a0_start, T1=100, T2=100,eps=0.1):
    res_a0, res_x0 = [], []
    res_a_9, res_x0_9 = [], []
    a0 = a0_start
    while a0 < a0_max:
        x_start = x0

        def foo(x0, func):
            change_par = False
            for _ in range(T1):
                x1 = func.f_with_param(x0)
                if x1 is None or x1 > 1 or x1 < 0:
                    change_par = True
                    break

                x0 = x1
            return x0, change_par

        x0, change_par = foo(x0, func)

        if not change_par:
            for _ in range(T2):
                x1 = func.f_with_param(x0) + eps*numpy.random.normal(0, 1)

                if x1 is None or x1 > 1 or x1 < 0:
                    break

                x0 = x1
                res_x0.append(x0)
                res_a0.append(a0)

        x0 = x_start
        a0 += 0.001
        func.set_a0(a0)

    return res_a0, res_x0


# для а0
a0_min = 1.4
a0_max = 4
b = 2.9

x0 = 0.3
label_param = "a"
eps = 0.01


"""for a"""
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)
res_b, res_x0 = bifurcation_a(func=myf, x0=x0, a0_max=a0_max, a0_start=a0_min, eps=eps)
plt.scatter(res_b, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")
export_two_arr(res_b, res_x0, file_name=f"bif_noise_by_{label_param}_{x0}_{eps}", folder="бифуркации/data")


"запуск с двух точек"
x0 = 0.7
"""for a"""
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)
res_b, res_x0 = bifurcation_a(func=myf, x0=x0, a0_max=a0_max, a0_start=a0_min, eps=eps)
plt.scatter(res_b, res_x0, label=f"x0={x0}", color='red', linewidths=0.01, marker=".")
export_two_arr(res_b, res_x0, file_name=f"bif_noise_by_{label_param}_{x0}_{eps}", folder="бифуркации/data")


plt.legend()
plt.grid(True)
plt.xlim([a0_min, a0_max])
plt.ylim([0, 1])
plt.xlabel(label_param)
plt.ylabel('p')
plt.show()
