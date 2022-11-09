from matplotlib import pyplot as plt

from Figure import MyFunction


def draw_lamerey(func: MyFunction, x0, show=False, label="",):
    x_start = x0
    res_x, res_y = [], []
    f = False
    if f:
        for _ in range(1000):
            x1 = func.f_with_param(x0)
            if x1 is None:
                print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
                break
            x0 = x1

    for _ in range(1, 51):
        x1 = func.f_with_param(x0)
        if x1 is None:
            print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
            break

        res_x += [x0, x0, x0, x1]
        res_y += [x0, x1, x1, x1]
        x0 = x1

    plt.plot(res_x, res_y, color='blue', label=f"$p_0$={x_start}")

    func.draw_function(title=label)
    func.draw_xy()
    # if show:
    #     plt.show()show


"""Построение с конкретными параметрами: """

al = 4
v = 0.5
ga = 0.2
el = 0.1
a0 = 3.3811
b = 2.896
myf = MyFunction(a=al, v=v, ga=ga, el=el, a0=a0, b=b)
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=1.4, b=2.9)
draw_lamerey(myf, show=True, x0=0.7)
plt.legend()

myf.draw_function(show=True, title=f"$𝛼_0={a0}, 𝛽={b}$")

# x0=0.25
# x0=0.2
