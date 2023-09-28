import numpy as np

'''
3.1.1:
we need the derivative of f(x) to be less than 1 for all x in a neighborhood of the root
'''

def bisection(f,fp,a,b,tol):
    
#    Inputs:
#     f,fp,a,b       - function, function derivative, and endpoints of initial interval
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
      fpd = fp(d)
      fd = f(d)
      if a < d - fd/fpd and d - fd/fpd < b:
        p0 = d
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
    
'''
3.1.3: I needed to change the inputs of Bisection to include the function f prime
'''

