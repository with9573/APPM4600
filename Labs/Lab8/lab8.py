import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: 1 / ( 1 + (10*x)**2 )
    a = -1
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend()
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show()
    
    

    
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

	'''create the intervals for piecewise approximations'''
	xint = np.linspace(a,b,Nint+1)
   
	'''create vector to store the evaluation of the linear splines'''
	yeval = np.zeros(Neval) 
    
    
	for jint in range(Nint):
		'''find indices of xeval in interval (xint(jint),xint(jint+1))'''
		'''let ind denote the indices in the intervals'''
        
		ind = np.array([xint[jint], xint[jint+1]])
        
		ind_xval = sub(xeval, xint)[jint]
        
		'''let n denote the length of ind'''
		n = len(ind_xval)
        
		'''temporarily store your info for creating a line in the interval of interest'''
		a1= xint[jint]
		fa1 = f(a1)
		b1 = xint[jint+1]
		fb1 = f(b1)
        
		for kk in range(n):
			'''use your line evaluator to evaluate the lines at each of the points in the interval'''
           
			'''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with the points (a1,fa1) and (b1,fb1)'''
			yeval[ind_xval[kk]] = line_form(a1, b1, fa1, fb1)(xeval[ind_xval[kk]])
	return yeval
           
           
def sub(xeval, xint):
	subs = []
	
	for i in range(len(xint) - 1):
		if i == len(xint) - 2:
			a = np.where( np.logical_and( (xeval <= xint[i + 1]), (xeval >= xint[i]) ) ) 

		else:
			a = np.where( np.logical_and( (xeval < xint[i + 1]), (xeval >= xint[i]) ) ) 
		subs.append(a)
	
	return subs

def line_form(x1, x2, f1, f2):
	fail = lambda x: 0
	if x1 == x2:
		print("fail")
		return fail
	
	m = (f2 - f1) / (x2 - x1)
	
	suc = lambda x: m*(x - x1) + f1
	
	return suc

def solve_M(f, x):
	y = np.zeros(len(x) - 1)
	
	for i in range(len(x)):
		y[i] = (f[i+2] - 2*f[i+1] + f[i]) / 2*(x[i+1] - x[1])**2
	
	cof = np.zeros( (len(x) - 1)**2 )
	cof.reshape( len(x) - 1, len(x) - 1)
	
	for i in range(len(x) - 1):
		for j in range(len(x) - 1):
			if i == j:
				cof[i][j] = 1/3
			if i == j - 1:
				cof[i][j] = 1/12
			if i == j+1:
				cof[i][j] = 1/12
	
	M = np.inv(cof)*y
	
	return M

def driver2():
	y = line_form(0,1,0,1)
	x = np.linspace(-1,2,30)
		
	plt.plot(x,y(x))
	plt.show()

def driver3():
	xeval = np.linspace(0,10,1000)
	xint = np.linspace(0,10,11)
	
	subs = sub(xeval, xint)
	
	print(subs)
		
	

driver()               
