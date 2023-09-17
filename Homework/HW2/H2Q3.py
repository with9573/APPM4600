import numpy as np
import math

def func(x):
    y = math.e**x
    return y-1


def approx(x, n):
    sum = 0
    for i in range(20):
        sum += (x**n)/math.factorial(i)
    return sum


def driver1():
    print(func(9.999999995000000e-10))

def driver2():
    sum = 0
    for i in range(20):
        sum += approx(9.999999995000000e-10, i)
    print(sum)

def driver3():
        print((approx(9.999999995000000e-10, 4) - func(9.999999995000000e-10))/approx(9.999999995000000e-10, 4))
    


driver3()
