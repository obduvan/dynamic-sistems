
from matplotlib import pyplot as plt
from Figure import MyFunction
from export_to_matlab import export_two_arr


def plt_show():
    plt.legend()
    plt.grid(True)
    # plt.xlim([a0_min, a0_max])
    plt.ylim([0, 1])
    plt.xlabel("a")
    plt.ylabel('p')
    plt.show()


def find_9_a0(func: MyFunction, x0, a0_max, a0_min, a0_start, T1=100, T2=100):
    res_a0, res_x0 = [], []
    x_first = x0
    a0 = a0_start

    while a0 < a0_max:
        # x_start = x0

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
            res_x0.append(x0)
            res_a0.append(a0)

        # x0 = x_start
        a0 += 0.00001
        func.set_a0(a0)

    x0 = x_first
    a0 = a0_start
    func.set_a0(a0)
    # #
    # plt.scatter(res_a0, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")
    # plt_show()
    while a0 > a0_min:
        # x_start = x0

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
            res_x0.append(x0)
            res_a0.append(a0)


        # x0 = x_start
        a0 -= 0.00001
        func.set_a0(a0)

    plt.scatter(res_a0, res_x0, label=f"x0={x_first}", color='black', linewidths=0.01, marker=".")
    plt_show()

    return res_a0, res_x0


b_fix = 2.9

"""отрезок где пересекается 9 и 4"""
# a0_min = 3.35
# a0_start = 3.43
#

# x0 = 0.3
# label_param = "a"

"4 only"
# a0_max = 3.5
# a0_min = 3.381
# a0_start = 3.43
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_start, b=b_fix)
# res_b, res_x = find_9_a0(func=myf, x0=0.3, a0_max=a0_max, a0_start=a0_start, a0_min=a0_min)
# export_two_arr(res_b, res_x, "4_only", "find_cycles_fix_b")


"14"
# x0 = 0.3
# a0_max = 3.377
# a0_min = 3.3468
# a0_start = 3.36
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_start, b=b_fix)
# res_b, res_x = find_9_a0(func=myf, x0=0.3, a0_max=a0_max, a0_start=a0_start, a0_min=a0_min)
# export_two_arr(res_b, res_x, "14_only", "find_cycles_fix_b")


"9_1"
# x0 = 0.72646

# x0 = 0.3
# a0_max = 3.3887
# a0_min = 3.37854
# a0_start = 3.38
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_start, b=b_fix)
# res_b, res_x = find_9_a0(func=myf, x0=x0, a0_max=a0_max, a0_start=a0_start, a0_min=a0_min)
# export_two_arr(res_b, res_x, "9_only", "find_cycles_fix_b")
# x_values_9 = {0.68471, 0.59511, 0.44839, 0.27354, 0.39977, 0.62288, 0.56327, 0.34934, 0.42243}



"9"
x0 = 0.7
a0_max = 3.3888
a0_min = 3.37854
a0_start = 3.38
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_start, b=b_fix)
res_b, res_x = find_9_a0(func=myf, x0=x0, a0_max=a0_max, a0_start=a0_start, a0_min=a0_min)
export_two_arr(res_b, res_x, "9_1_only", "find_cycles_fix_b")
# x_values_9_1 = {0.72646, 0.60023, 0.37712, 0.55161, 0.43673, 0.65066, 0.57757, 0.31529, 0.40489}


