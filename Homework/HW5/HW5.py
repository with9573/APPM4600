import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm

def evalF(x):
	F = np.zeros(2)
	F[0] = 3*(x[0])**2 - (x[1])**2
	F[1] = 3*x[0]*(x[1])**2 - (x[0])**3 - 1
	return F
	
def evalJ(x):
	J = np.array([ [6*x[0], -2*x[1] ], [3*(x[1])**2 - 3*(x[0])**2, 6*x[0]*x[1] ] ])
	return J

def NewtonModified(x0,tol,Nmax):
	for its in range(Nmax):
		J = np.array([ [1/6, 1/18], [0, 1/6] ])
		F = evalF(x0)
		x1 = x0 - J.dot(F)
		if (norm(x1-x0) < tol):
			xstar = x1
			ier =0
			return[xstar, ier, its]
		x0 = x1
	xstar = x1
	ier = 1
	return[xstar,ier,its]
	
def Newton(x0,tol,Nmax):
	for its in range(Nmax):
		J = evalJ(x0)
		Jinv = inv(J)
		F = evalF(x0)
		x1 = x0 - Jinv.dot(F)
		if (norm(x1-x0) < tol):
			xstar = x1
			ier =0
			return[xstar, ier, its]
		x0 = x1
	xstar = x1
	ier = 1
	return[xstar,ier,its]

def driver1():
	x = [1,1]
	
	[xstar,ier,its] = Newton(x,1e-10,100)
	print(xstar, ier)





def f(x):
	return (x[0])**2 + 4*(x[1])**2 + 4*(x[2])**2 - 16

def d(x):
	return f(x) / ( (2*x[0])**2 + (8*x[1])**2 + (8*x[2])**2 )

def xx(x):
	return x[0] - d(x)*2*x[0]

def yy(x):
	return x[1] - d(x)*8*x[1]

def zz(x):
	return x[2] - d(x)*8*x[2]

def iteration(x, tol, Nmax):
	col = np.array(x)
	
	
	for i in range(Nmax):
		if f(x) == 0:
			print("equal")
			return [x, col, 0]
		
		x[0] = xx(x)
		x[1] = yy(x)
		x[2] = zz(x)
		
		col = np.append( col, [x[0], x[1], x[2]] )
		
		#if norm( col[i+1] - col[i] ) < tol:
			#print("tol")
			#return [x, col, 0]
	
	return [x, col, 1]

def driver3():
	x = [1,1,1]
	[xstar, col, ier] = iteration(x, 1e-100, 100)
	print(xstar, ier)
	print(col)
driver3()
		
		
	
	



