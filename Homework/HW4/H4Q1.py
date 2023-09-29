import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]


def newton(f,fp,p0,tol,Nmax):
	p = np.zeros(Nmax+1);
	p[0] = p0
	for it in range(Nmax):
		p1 = p0-f(p0)/fp(p0)
		p[it+1] = p1
		if (abs(p1-p0) < tol):
			pstar = p1
			info = 0
			return [p,pstar,info,it]
		p0 = p1
	pstar = p1
	info = 1
	return [p,pstar,info,it]


def f(x):
	return 35*sp.special.erf(x/(2*np.sqrt(0.138e-6*5.184e6))) - 15

def fp(x):
	return 35/(2*np.sqrt(0.138e-6*5.184e6))*np.exp((-x/(2*np.sqrt(0.138e-6*5.184e6)))**2)
	
def driver():
	x = np.arange(0,2,0.001)
	plt.plot(x, f(x))
	plt.show()

def driver2():
	f = lambda x: 35*sp.special.erf(x/(2*np.sqrt(0.138e-6*5.184e6))) - 15
	[astar, ier] = bisection(f,0,2,1e-13)
	print(astar, ier)

def driver3():
	f = lambda x: 35*sp.special.erf(x/(2*np.sqrt(0.138e-6*5.184e6))) - 15
	fp = lambda x: 35/(2*np.sqrt(0.138e-6*5.184e6))*np.exp((-x/(2*np.sqrt(0.138e-6*5.184e6)))**2)
	
	[p,pstar,info,it] = newton(f,fp,2,1e-13,100)
	print(pstar,info)
	
driver3()