import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv

def driver():



	f = lambda x: 1/(1 + 100*x**2)

	N = 3

	a = -1
	b = 1
   
   

	xint = np.linspace(a,b,N+1)
    

	yint = f(xint)
    

	Neval = 1000
	xeval = np.linspace(a,b,Neval+1)
	yeval_l= np.zeros(Neval+1)
	yeval_dd = np.zeros(Neval+1)
	yeval_m = np.zeros(Neval+1)
    
	Vinv = inv(VM(N, xint)) 
	a = np.matmul(Vinv, np.transpose(yint))
    
	for i in range(Neval + 1):
		s = 0
		for j in range(N+1):
			s = s + a[j]*xeval[i]
		yeval_m[i] = s


	plt.figure()    
	plt.plot(xeval,yeval_m,'ro-')
	plt.show()		
    
    

	y = np.zeros( (N+1, N+1) )
     
	for j in range(N+1):
		y[j][0]  = yint[j]

	y = dividedDiffTable(xint, y, N+1)

	for kk in range(Neval+1):
		yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
		yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
          

    



	fex = f(xeval)
       

	plt.figure()    
	plt.plot(xeval,fex,'ro-')
	plt.plot(xeval,yeval_l,'bs--') 
	plt.plot(xeval,yeval_dd,'c.--')
	plt.legend()

	plt.figure() 
	err_l = abs(yeval_l-fex)
	err_dd = abs(yeval_dd-fex)
	plt.semilogy(xeval,err_l,'ro--',label='lagrange')
	plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
	plt.legend()
	plt.show()
   

def VM(N, xint):
	V = np.zeros((N+1)**2)
	np.reshape(V, (N+1,N+1))
	
	for i in range(N+1):
		for j in range(N+1):
			V[i][j] = (xint[i])**j
	return V

def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

       

driver()       