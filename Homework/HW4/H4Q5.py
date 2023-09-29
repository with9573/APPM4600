import numpy as np
import matplotlib.pyplot as plt

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

def driver():
	f = lambda x: x**6 - x - 1
	fp = lambda x: 6*x**5 - 1
	
	[p,pstar,info,it] = newton(f,fp,2,1e-10,8)
	
	for i in range(9):
		p[i] = p[i] - pstar
	
	p2 = np.zeros(9)
	for i in range(1,8):
		p2[i] = p[i]
	
	plt.plot(p,p2)
	plt.show()
		

driver()