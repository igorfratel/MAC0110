#.n Igor Fratel Santana
#.u 9793565

from math import pi,sin,cos,log
import matplotlib.pyplot as plt

def  transformacaoEscala(U, V, n, a, b):
	i=0
	while i<n:
		V[i] = a+U[i]*(b-a+1)
		i+=1
	return V

def somaVetores(U1,U2,U,n):
    i=0
    while i<n:
        U[i] = U1[i]+U2[i]
        i+=1
    return U
	
def raizVetor(U,n):
	i=0
	while i<n:
		U[i] = U[i]**(1/2)
		i+=1
	return U

def normalTransform(U1,U2,Z1,Z2,n):
	i=0
	while i<n:
	    Z1[i] = cos(2*pi*U2[i])*((-2*log(U1[i]))**(1/2))
	    Z2[i] = sin(2*pi*U2[i])*((-2*log(U1[i]))**(1/2))
	    i+=1
	return Z1,Z2

def histogram(U,m):

    return plt.hist(U,m,facecolor='r',alpha=0.3)
    
	