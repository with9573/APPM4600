import numpy as np

def fixedpt(f,x0,tol,N):
	vec = np.zeros((N,1))
	for i in range(N):
		x1 = f(x0)
		vec[i] = x1
		if abs(x1 - x0) < tol:
			xstar = x1
			ier = 0
			return [vec, xstar, ier, i + 1]
		x0 = x1
	xstar = x1
	ier = 1
	return [vec, xstar, ier, N]

def pretest():
	#test1
	f1 = lambda x: x + 4
	[vec1, ier1, iteration1] = fixedpt(f1, 1, 1e-10, 10)
	print(vec1)
	print(ier1)
	print(iteration1)

def lab322(pn, tol):
	vec = np.zeros((len(pn),1))
	for i in range(len(pn)-2):
		vec[i] = pn[i] - ( (pn[i+1] - pn[i])**2 ) / ( pn[i+2] - 2*pn[i+1] + pn[i] )
		if abs(vec[i] - vec[i-1]) < tol:
			return [vec, i]
	return [vec, 999]
		
def test322():
	f1 = lambda x: x**2
	[vec1, xstar1, ier1, iteration1] = fixedpt(f1, 0.5, 1e-10, 10)
	print(vec1, xstar1, ier1, iteration1)
	[vec2, it2] = lab322(vec1, 1e-10)
	print(vec2, it2)
	
def test323():
	f = lambda x: (10 / (x + 4) )**(1/2)
	[vec1, xstar1, ier1, iteration1] = fixedpt(f, 1.5, 1e-10, 20)
	print(vec1, xstar1, ier1, iteration1)
	[vec2, it2] = lab322(vec1, 1e-10)
	print(vec2, it2)
	
test323()