import numpy as np
import matplotlib.pyplot as plt
import math


def func1(x):
    return x**9 -18*x**8 +144*x**7 -672*x**6 +2016*x**5 -4032*x**4 +5376*x**3 -4608*x**2 +2304**x -512

def driver1():
    x = np.arange(1.920,2.080,0.001)
    ya = func1(x)
    yb = (x-2)**9

    #plt.plot(x,ya)
    plt.plot(x,yb)
    plt.show()


driver1()
