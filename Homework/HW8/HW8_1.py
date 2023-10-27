import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math

def driver():


    f = lambda x: 1./(1.+x**2)
    fp = lambda x: -2*x/(1.+x**2)**2

    N = 19
    ''' interval'''
    a = -5
    b = 5
   
    ''' create equispaced interpolation nodes'''
    #xint = np.zeros(N + 1)
    #for i in range(1,N+2):
    	#xint[i - 1] = 5*math.cos( (2*i - 1)*math.pi / (2*(N+1)) )
    
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = np.zeros(N+1)
    ypint = np.zeros(N+1)
    for jj in range(N+1):
        yint[jj] = f(xint[jj])
        ypint[jj] = fp(xint[jj])
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yevalL = np.zeros(Neval+1)
    yevalH = np.zeros(Neval+1)
    for kk in range(Neval+1):
      yevalL[kk] = eval_lagrange(xeval[kk],xint,yint,N)
      yevalH[kk] = eval_hermite(xeval[kk],xint,yint,ypint,N)

    ''' create vector with exact values'''
    fex = np.zeros(Neval+1)
    for kk in range(Neval+1):
        fex[kk] = f(xeval[kk])
    
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yevalL,'c.--',label='Lagrange') 
    plt.semilogy()
    plt.legend()
    title = "Lagrange vs f(x) for " + str(N+1) + " nodes"
    plt.title(title)
    plt.show()
         
    errL = abs(yevalL-fex)
    plt.figure()
    plt.semilogy(xeval,errL,'bs--',label='Lagrange')
    plt.legend()
    title = "Lagrange absolute error for " + str(N+1) + " nodes"
    plt.title(title)
    plt.show()            
    
    
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yevalH,'c.--',label='Hermite')
    plt.semilogy()
    plt.legend()
    title = "Hermite vs f(x) for " + str(N+1) + " nodes"
    plt.title(title)
    plt.show()
         
    errH = abs(yevalH-fex)
    plt.figure()
    plt.semilogy(xeval,errH,'c.--',label='Hermite')
    plt.legend()
    title = "Hermite Absolute Error for " + str(N+1) + " nodes"
    plt.title(title)
    plt.show()     


def eval_hermite(xeval,xint,yint,ypint,N):

    ''' Evaluate all Lagrange polynomials'''

    lj = np.ones(N+1)
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    ''' Construct the l_j'(x_j)'''
    lpj = np.zeros(N+1)
#    lpj2 = np.ones(N+1)
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
           	lpj[count] = lpj[count]+ 1./(xint[count] - xint[jj])
#              lpj2[count] = lpj2[count]*(xint[count] - xint[jj])
              #lpj[count] = lpj[count]+ 1./(xint[count] - xint[jj])
              

    yeval = 0.
    
    for jj in range(N+1):
       Qj = (1.-2.*(xeval-xint[jj])*lpj[jj])*lj[jj]**2
       Rj = (xeval-xint[jj])*lj[jj]**2
#       if (jj == 0):
#         print(Qj)
         
#         print(Rj)
#         print(Qj)
#         print(xeval)
 #        return
       yeval = yeval + yint[jj]*Qj+ypint[jj]*Rj
       
    return(yeval)
       


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
  
    

       

driver()        
