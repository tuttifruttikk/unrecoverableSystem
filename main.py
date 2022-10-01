import math
import random
import matplotlib.pyplot as plt

n = 30000
p1 = 0.6
p2 = 1 - p1
l1 = 0.9
l2 = 1.5
T = []


def average_t():
    tmp = 0
    for i in range(len(T)):
        tmp += T[i]
    return tmp / n


def time_modeling1():
    for i in range(n):
        tmp = random.random()
        if i / n - p1 < 0.01:
            T.append(-math.log(tmp) / l1)
        else:
            T.append(-math.log(tmp) / l2)


def time_modeling2():
    for i in range(n):
        tmp1 = (-math.log(random.random())) / l1
        tmp2 = (-math.log(random.random())) / l2
        T.append(min(tmp1, tmp2))


def time_modeling3():
    for i in range(n):
        tmp1 = -math.log(random.random())
        tmp2 = -math.log(random.random())
        if tmp1 / l1 >= tmp2 / l2:
            T.append(tmp1 / l1)
        else:
            T.append(tmp2 / l2)


def find_n(t):
    nt = 0
    for i in range(len(T)):
        if t <= T[i]:
            nt += 1
    return nt


def theroretical(case, av_t):
    R_arr = []
    L_arr = []
    t_arr = []
    if case == 1:
        t = 0
        while t - av_t <= 0:
            t_arr.append(t)
            R = math.exp(-l1 * t) * p1 + math.exp(-l2 * t) * p2
            R_arr.append(R)
            l = (l1 * p1 * math.exp(-l1 * t) + l2 * p2 * math.exp(-l2 * t)) / R
            L_arr.append(l)
            t += 0.01
    elif case == 2:
        t = 0
        l = l1 + l2
        while t - av_t <= 0:
            t_arr.append(t)
            R = math.exp(-l1 * t) * math.exp(-l2 * t)
            R_arr.append(R)
            L_arr.append(l)
            t += 0.01
    elif case == 3:
        t = 0
        while t - av_t <= 0:
            t_arr.append(t)
            R = math.exp(-l1 * t) + math.exp(-l2 * t) - math.exp(-l1 * t) * math.exp(-l2 * t)
            R_arr.append(R)
            l = (-1) * (-l1 * math.exp(-l1 * t) - l2 * math.exp(-l2 * t) + (l1 +l2) * math.exp(-(l1 + l2) * t)) / R
            L_arr.append(l)
            t += 0.01
    return R_arr, L_arr, t_arr


def experimental(av_t):
    t = 0
    R_arr = []
    L_arr = []
    t_arr = []
    while t < av_t:
        t_arr.append(t)
    nt = find_n(t)
    R = nt / n
    R_arr.append(R)
    l = (nt - find_n(t + 0.001)) / (nt * 0.001)
    L_arr.append(l)
    t += 0.01
    return R_arr, L_arr, t_arr


def first_period():
    time_modeling1()
    tmp = average_t()
    r, l, t = experimental(tmp)
    rt, lt, tt = theroretical(1, tmp)
    plt.plot(t, r, label='Экспериментальное')
    plt.plot(tt, rt, label='Теоретическое')
    plt.legend()
    plt.grid()
    plt.savefig('1periodR(t).png')
    plt.show()
    plt.plot(t, l, label='Экспериментальное')
    plt.plot(tt, lt, label='Теоретическое')
    plt.legend()
    dots_x = [tt[0], tt[len(tt) - 1]]
    dots_y = [lt[0], lt[len(lt) - 1]]
    plt.plot(dots_x, dots_y, 'ro')
    plt.text(dots_x[0], dots_y[0], f'{round(lt[0], 4)}')
    plt.text(dots_x[1], dots_y[1], f'{round(lt[len(lt) - 1], 4)}')
    plt.grid()
    plt.savefig('1periodL(t).png')
    plt.show()
    T.clear()
    return t, r, rt, l, lt


def second_period():
    time_modeling2()
    tmp = average_t()
    r, l, t = experimental(tmp)
    rt, lt, tt = theroretical(2, tmp)
    plt.plot(t, r, label='Экспериментальное')
    plt.plot(tt, rt, label='Теоретическое')
    plt.legend()
    plt.grid()
    plt.savefig('2periodR(t).png')
    plt.show()
    plt.plot(t, l, label='Экспериментальное')
    plt.plot(tt, lt, label='Теоретическое')
    plt.legend()
    plt.grid()
    plt.savefig('2periodL(t).png')
    plt.show()
    T.clear()
    return t, r, rt, l, lt


def third_period():
    time_modeling3()
    tmp = average_t()
    r, l, t = experimental(tmp)
    rt, lt, tt = theroretical(3, tmp)
    plt.plot(t, r, label='Экспериментальное')
    plt.plot(tt, rt, label='Теоретическое')
    plt.legend()
    plt.grid()
    plt.savefig('3periodR(t).png')
    plt.show()
    plt.plot(t, l, label='Экспериментальное')
    plt.plot(tt, lt, label='Теоретическое')
    plt.legend()
    plt.grid()
    plt.savefig('3periodL(t).png')
    plt.show()
    T.clear()
    return t, r, rt, l, lt


def main():
    first_period()
    second_period()
    third_period()


if __name__ == '__main__':
    main()
