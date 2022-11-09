


import math

from Figure import MyFunction
from export_to_matlab import export_two_arr
import matplotlib.pyplot as plt

a0_min = 1.4
a0_max = 4
b = 2.9

x0 = 0.3
label_param = "a"
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)


def p1(a0):
    return 0.5 - (0.2*(4 - a0))/(0.2 - b)



def p5(a0):
    return 0.5 + (0.2*(4 - a0))/(0.2 - b)

res_a0, res_x0 = [], []


while a0_min < 4:
    p = p1(a0_min)
    res_x0.append(p)
    res_a0.append(a0_min)
    a0_min += 0.001



plt.scatter(res_a0, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")


plt.legend()
plt.grid(True)
plt.xlim([a0_min, a0_max])
plt.ylim([0, 1])
plt.xlabel(label_param)
plt.ylabel('p')
plt.show()







