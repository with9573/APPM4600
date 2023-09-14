# import libraries
import numpy as np

#def f(x):
#	return x**2(x-1)

def driver():

# use routines    
    f1 = lambda x: (x-1)*(x-3)*(x-5)
    f2 = lambda x: (x-1)**2*(x-3)
    f3 = lambda x: np.sin(x)
    
    a1 = 0
    b1 = 2.4
    
    a2 = 0
    b2 = 2
    
    a3 = 0
    b3 = 0.1
    
    a4 = 0.5
    b4 = 3*np.pi/4

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-5

    [astar1,ier1] = bisection(f1,a1,b1,tol)
    [astar2,ier2] = bisection(f2,a2,b2,tol)
    [astar3,ier3] = bisection(f3,a3,b3,tol)
    [astar4,ier4] = bisection(f3,a4,b4,tol)
    
    print('1. the approximate root is',astar1)
    print('the error message reads:',ier1)
    print('f(astar) =', f1(astar1))
    
    print('2. the approximate root is',astar2)
    print('the error message reads:',ier2)
    print('f(astar) =', f2(astar2))
    
    print('3. the approximate root is',astar3)
    print('the error message reads:',ier3)
    print('f(astar) =', f3(astar3))
    
    print('4. the approximate root is',astar4)
    print('the error message reads:',ier4)
    print('f(astar) =', f3(astar4))




# define routines
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
      
driver()         



"""
SOLUTIONS

Question 1, all three parts outputs

1. the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08

2. the approximate root is -1
the error message reads: 1
f(astar) = -2

3. the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08


each interval gives a returned root, whether or not it "believes" it to be true (error message), and an estimate for how far off the root is. 
The method was not successful for the middle interval because the interval did not contain the actual root. It knows this. it gave error message. I believe it is possible for bisection to find the root at x=0. 


Question 2, all four parts

1. the approximate root is 1.0000030517578122
the error message reads: 0
f(astar) = 2.4414006618542327e-05

2. the approximate root is 0
the error message reads: 1
f(astar) = -3

3. the approximate root is 0
the error message reads: 0
f(astar) = 0.0

4. the approximate root is 0.5
the error message reads: 1
f(astar) = 0.479425538604203


These are all answers that I understand and accept to be true and accurate. I believe it did achieve the desired accuracy

"""