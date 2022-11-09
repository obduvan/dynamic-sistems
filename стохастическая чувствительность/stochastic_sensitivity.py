import math

from Figure import MyFunction
from export_to_matlab import export_two_arr
import matplotlib.pyplot as plt


def get_w_p1_p5(a, b):
    return 1 / (1 - (1 - a + b)**2)


def get_w_p3(a0):
    return 1 / (1 - (1 - a0)**2)


def p_1_sens(p, w, eps):
    return p + 3 * eps * math.sqrt(w)


def p_2_sens(p, w, eps):
    return p - 3 * eps * math.sqrt(w)


def stohastic_sensivity(func: MyFunction, x0, a0_max, a0, eps, T1=100, T2=100, b=2.9, a=4):
    res_a0, res_x0 = [], []
    res_p1, res_p2 = [], []

    while a0 < a0_max:
        x_start = x0

        def foo(x0, func):
            for _ in range(T1):
                x1 = func.f_with_param(x0)
                if x1 is None or x1 > 1 or x1 < 0:
                    break
                x0 = x1
            return x0

        x0 = foo(x0, func)

        for _ in range(T2):
            x1 = func.f_with_param(x0)
            if x1 is None or x1 > 1 or x1 < 0:
                break

            x0 = x1
            # w = get_w_p1_p5(a, b)
            w = get_w_p3(a0)
            if w >= 0:
                p1 = p_1_sens(p=x0, w=w, eps=eps)
                p2 = p_2_sens(p=x0, w=w, eps=eps)
                res_p1.append(p1)
                res_p2.append(p2)
                res_x0.append(x0)
                res_a0.append(a0)

        x0 = x_start
        a0 += 0.001
        func.set_a0(a0)

    return res_a0, res_x0, res_p1, res_p2


a0_min = 1.4
a0_max = 2

b = 2.9

x0 = 0.47
label_param = "a"
eps = 0.01
p1_label = "p1"
p2_label = "p2"
folder = f"стохастическая чувствительность/stoh_senc_{eps}"

"""for a"""
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)
res_a0, res_x0, res_p1, res_p2 = stohastic_sensivity(func=myf, x0=x0, a0_max=a0_max, a0=a0_min, eps=eps)
plt.scatter(res_a0, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")
plt.scatter(res_a0, res_p1, color='black', linewidths=0.01, marker=".")
plt.scatter(res_a0, res_p2, color='gray', linewidths=0.01, marker=".")
export_two_arr(res_a0, res_x0, file_name=f"stoh_senc_{label_param}_{x0}", folder=folder)
export_two_arr(res_a0, res_p1, file_name=f"stoh_senc_{p1_label}_{x0}", folder=folder)
export_two_arr(res_a0, res_p2, file_name=f"stoh_senc_{p2_label}_{x0}", folder=folder)



"""for a"""
# x0 = 0.7
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)
# res_a0, res_x0, res_p1, res_p2 = stohastic_sensivity(func=myf, x0=x0, a0_max=a0_max, a0=a0_min, eps=eps)
# plt.scatter(res_a0, res_x0, label=f"x0={x0}", color='red', linewidths=0.01, marker=".")
# plt.scatter(res_a0, res_p1, color='pink', linewidths=0.01, marker=".")
# plt.scatter(res_a0, res_p2, color='orange', linewidths=0.01, marker=".")
# # export_two_arr(res_a0, res_x0, file_name=f"stoh_senc_{label_param}_{x0}", folder=folder)
# export_two_arr(res_a0, res_p1, file_name=f"stoh_senc_{p1_label}_{x0}", folder=folder)
# export_two_arr(res_a0, res_p2, file_name=f"stoh_senc_{p2_label}_{x0}", folder=folder)

plt.legend()
plt.grid(True)
plt.xlim([a0_min, a0_max])
plt.ylim([0, 1])
plt.xlabel(label_param)
plt.ylabel('p')
plt.show()
