import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math

def dotProduct(x,y,n):
    
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
        
    return dp

def driver1():
    print('Driver1')
    print('**********')

    n = 100
    x = np.linspace(0,np.pi,n)

# this is a function handle. You can use it to define
# functions instead of using a subroutine like you
# have to in a true low level language.
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    
    y = f(x)
    w = g(x)
    
# evaluate the dot product of y and w
    dp = dotProduct(y,w,n)

# print the output

    print('the dot product is : ', dp)
    print('**********')

    return

def driver2():
    print('Driver2')
    print('**********')
    
    x = [1,2,3]
    print(x*3)

    y = np.array([1,2,3])

    print(y*3)
    
    print('**********')
    
    return

def driver3():
    print('Driver3')
    print('**********')
    print('(image)')

    X = np.linspace(0, 2 * np.pi, 100)
    Ya = np.sin(X)
    Yb = np.cos(X)
    plt.plot(X, Ya)
    plt.plot(X, Yb)
    plt.show()
    
    print('**********')

def driver4():

    x = np.linspace(0,9,10)
    y = np.arange(0,10,1)

    print('x:',x)
    print('y:',y)

    print('first three entries in x:', x[0], x[1], x[2])
    print('first three entries in y:', y[0], y[1], y[2])

    w = 10**(-np.linspace(1,10,10))

    print('w:',w)

    x2 = np.linspace(1,10,10)

    print('x2:', x2)

    s = 3*w

    plt.semilogy(x2,w)
    plt.semilogy(x2,s)
    plt.show()
    
#driver1()
#driver2()
#driver3()
driver4()






