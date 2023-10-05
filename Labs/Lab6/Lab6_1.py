import numpy as np
import math
from numpy.linalg import inv
from numpy.linalg import norm

def driver1():
	h = 0.01 * 2.**(-np.arange(0, 10))
	
	f = lambda x: math.cos(x)
	
	pio2 = math.pi / 2
	
	for i in range(len(h)):
		print("method 1:", (f(pio2 + h[i]) - f(pio2)) / h[i])

	for i in range(len(h)):
		print("method 2:", (f(pio2 + h[i]) - f(pio2 - h[i])) / (2*h[i]))



def array_compare(a,b):
	return norm(a-b)
	
def evalF(x):
	F = np.zeros(2)
	
	F[0] = 4*(x[0])**2 + (x[1])**2 - 4
	F[1] = x[0] + x[1] - math.sin(x[0] - x[1])
	return F

def evalJ(x):
	J = np.array([ [ 8*x[0], 2*x[1] ], [ 1 - math.cos(x[0] - x[1]), 1 + math.cos(x[0] - x[1])] ])
	return J
	

def SlackerNewton(x0,tol,Nmax, root):
	''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
	''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its, root = known root array of function'''
	''' Outputs: xstar= approx root, ier = error message, its = num its'''

	"THE IDEA: at each iteration, if the error of xn+1 / error of xn is greater than 1, recompute the jacobian inverse"
	"MY CODE HAS ERRORS SINCE IT DIVIDES BY ONE, BUT I FEEL LIKE THE IDEA IS MOSTLY-IMPLEMENTED. ERIN USED THE METHOD OF COMPARING THE NORMS OF ERRORS, KNOWING THE ROOT, AND TONY TAKES THE NORM VERSUS X1 AND X2, AND IF ABOVE A CERTAIN CONDITION NUMBER, RERUN THE INVERSE/JACOBINAN. EVERYONE HAD ERRORS BUT WE FEEL CONFIDENT FOR THE MOST PART."
	J = evalJ(x0)
	Jinv = inv(J)
	count = 1
	for its in range(Nmax):
		F = evalF(x0)
		x1 = x0 - Jinv.dot(F)
		if (norm(x1-x0) < tol):
			xstar = x1
			ier =0
			return[xstar, ier,its, count]
		if ( array_compare(x1,root) / array_compare(x0,root)) > 1:
			J = evalJ(x1)
			Jinv = inv(J)
			count += 1
		x0 = x1
	xstar = x1
	ier = 1
	return[xstar,ier,its, count]
	
	
def driver2():
	x = np.array( [1,0] )
	
	[xstar,ier,its,count] = SlackerNewton(x, 10e-10, 100, [1,0])
	print(count)
	
driver2()
	