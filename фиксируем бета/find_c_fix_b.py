from matplotlib import pyplot as plt

from Figure import MyFunction
from export_to_matlab import export_two_arr


def c1(func: MyFunction):
    return func.v - func.ga


def c2(func: MyFunction):
    return func.v - func.el


def c3(f: MyFunction):
    return f.v + f.el


def c4(f: MyFunction):
    return f.v + f.ga


def left_central(f: MyFunction):
    return f.v - f.el + 0.00001


def right_central(f: MyFunction):
    return f.v + f.el - 0.00001


def find_c(func: MyFunction, a0, a0_max, func_c, label):
    res_a0_c, res_p_c = [], []
    res_a0_fc, res_p_fc = [], []

    while a0 < a0_max:
        f_c = func_c(func)
        f_c1 = func.f_with_param(f_c)
        res_p_c.append(f_c1)
        res_a0_c.append(a0)

        p = func.f_with_param(f_c1)
        res_p_fc.append(p)
        res_a0_fc.append(a0)

        a0 += 0.001
        func.set_a0(a0)

    export_two_arr(res_a0_c, res_p_c, f"{label}", folder="фиксируем бета")
    export_two_arr(res_a0_fc, res_p_fc, f"f({label})", folder="фиксируем бета")
    plt.scatter(res_a0_c, res_p_c, label=f"{label}", color='green', linewidths=0.01, marker=".")
    plt.scatter(res_a0_fc, res_p_fc, label=f"f({label})", color='red', linewidths=0.01, marker=".")


a0 = 2.9
a0_max = 4
b_fix = 2.9

label_param = "a0"
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b_fix)

find_c(func_c=right_central, a0=a0, a0_max=a0_max, func=myf, label="right_central")

plt.legend()
plt.grid(True)
# plt.xlim([b, b_max])
plt.ylim([0, 1])
plt.xlabel(label_param)
plt.ylabel('p')
plt.show()
