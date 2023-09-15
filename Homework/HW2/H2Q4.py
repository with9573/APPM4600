import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import math


pi = math.pi

def q1():
    t = np.arange(0, pi, pi/30)
    def fun(n):
        return math.cos(n)
    fun = np.vectorize(fun)
    y = fun(t)

    sum = 0

    for i in range(len(t)):
        sum += t[i]*y[i]

    print("the sum is:", sum)

def q2():
    x = lambda a: 1.2*(1+0.1*math.sin(15*a + 0))*math.cos(a)
    y = lambda a: 1.2*(1+0.1*math.sin(15*a + 0))*math.sin(a)

    a_range = np.arange(0, pi, 0.01)
    for a in a_range:
        plt.plot(x(a),y(a), markersize=3, marker='o')
    plt.show()

def q2b():
    def x(R, r, f, a, p):
        return R*(1+r*math.sin(f*a + p))*math.cos(a)
    def y(R, r, f, a, p):
        return R*(1+r*math.sin(f*a + p))*math.sin(a)

    a_range = np.arange(0, pi, 0.01)
    #p = np.random.uniform
    for a in a_range:
        for i in range(10):
            plt.plot(x(i, 0.05, 2+i, a, np.random.random()), y(i, 0.05, 2+i, a, np.random.random()), markersize = 3, marker = 'o')
    plt.show()
q1()
q2()
q2b()
