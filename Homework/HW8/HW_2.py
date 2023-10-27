import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():
    
    f = lambda x: math.sin(10*x)
    fp = lambda x: 10*math.cos(10*x)
    a = 0
    b = 2*math.pi
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval+1)
    
    ''' number of intervals'''
    Nint = 19
    xint = np.linspace(a,b,Nint+1)
    #xint = np.zeros(Nint + 1)
    #for i in range(1,Nint+2):
    	#xint[Nint + 1 - i] = 5*math.cos( (2*i - 1)*math.pi / (2*(Nint+1)) )
    yint = f(xint)
    ypint = np.array( [fp(xint[0]), fp(xint[Nint]) ] )

    
    
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
    
    print('M =', M)
#    print('C =', C)
#    print('D=', D)
    
    yeval = eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D)
    
    print('yeval = ', yeval)
    
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
        
    nerr = norm(fex-yeval)
    print('nerr = ', nerr)
    
    plt.figure()    
    plt.plot(xeval,fex,'ro-',label='exact function')
    plt.plot(xeval,yeval,'c.--',label='natural spline') 
    plt.legend()
    title = "Clamped Spline vs f(x) for " + str(Nint + 1) + " nodes"
    plt.title(title)
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure() 
    plt.semilogy(xeval,err,'ro--')
    plt.legend()
    title = "Clamped Spline error for " + str(Nint + 1) + " nodes"
    plt.title(title)
    plt.show()
    
def create_natural_spline(yint,xint,N,ypint):

#    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    #b[0] = -ypint[0] + (yint[1]-yint[0])/h[0]
    b[0] = -ypint[0] 
    #b[N] = -ypint[1] + (yint[N]-yint[N-1])/h[N-1]
    b[N] = -ypint[1] 
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N+1,N+1))
    A[0][0] = h[0]/3
    for j in range(1,N):
       A[j][j-1] = h[j-1]/6
       A[j][j] = (h[j]+h[j-1])/3 
       A[j][j+1] = h[j]/6
    A[N][N] = h[N-1]/3

    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,C,D):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    hi = xip-xi
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
            + C*(xip-xeval) + D*(xeval-xi)
    return yeval 
    
    
def  eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D):
    
    yeval = np.zeros(Neval+1)
    
    for j in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        atmp = xint[j]
        btmp= xint[j+1]
        
#   find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        print(ind)
        xloc = xeval[ind]

# evaluate the spline
        yloc = eval_local_spline(xloc,atmp,btmp,M[j],M[j+1],C[j],D[j])
#        print('yloc = ', yloc)
#   copy into yeval
        yeval[ind] = yloc

    return(yeval)
           
driver()               

