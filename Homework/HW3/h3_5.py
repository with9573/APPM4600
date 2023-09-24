import numpy as np
import matplotlib.pyplot as plt

def driver():
	x = np.arange(-2, 8, 0.01)
	y = lambda k: k - 4*np.sin(2*k) - 3
	
	plt.plot(x,y(x))
	plt.show()

# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, count]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, count]
    
def driver2():
	f = lambda x: 5*x/4 - np.sin(2*x) - 3/4	
	[xstar, ier, count] = fixedpt(f,2, 1e-10,100)
	print("root:", xstar)
	print(ier)

driver2()