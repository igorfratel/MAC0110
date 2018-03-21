#.n Igor Fratel Santana
#.u 9793565
from random import random
#importando as funções do outro arquivo
from EP3_transformacoes_sobre_listas_uniformes import *
import matplotlib.pyplot as plt
import numpy as np

#pedir os valores e criar as listas necessarias
n=int(input('n: '))
m=int(input('m: '))
a=float(input('a: '))
b=float(input('b: '))
i=0
list_unif=[]
list_unif2=[]
list_zerada=[]
list_zerada2=[]
while i<n:
    list_unif.append(random())
    list_unif2.append(random())
    list_zerada.append(0)
    i+=1
#plotando o primeiro histograma
plt.figure(figsize=(7, 7), dpi=80)
resultante = transformacaoEscala(list_unif,list_zerada, n, a, b)
histogram(resultante,m)
plt.title('hist_escala_transalacao')
plt.savefig('hist_escala_transalacao.png')

#plotando o segundo histograma
plt.figure(figsize=(7,7), dpi=80)
resultante = somaVetores(list_unif,list_unif2,list_zerada,n)
histogram(resultante,m)
plt.title('hist_soma')
plt.savefig('hist_soma.png')

#'resetando' uma lista que foi modificada nas operações anteriores
i=0
while i<n:
    list_unif[i]=random()
    i+=1

#plotando o terceiro histograma
plt.figure(figsize=(7, 7), dpi=80)
resultante = raizVetor(list_unif,n)
histogram(resultante,m)
plt.title('hist_raiz')
plt.savefig('hist_raiz.png')

#'resetando' listas modificadas pelas operações anteriores 
i=0
while i<n:
	list_unif[i]=random()
	list_unif2[i]=random()
	list_zerada[i]=0
	list_zerada2.append(0)
	i+=1

#plotando o quarto histograma(partes 1 e 2)
plt.figure(figsize=(7, 7), dpi=80)
normalTransform(list_unif,list_unif2,list_zerada,list_zerada2,n)
histogram(list_zerada,m)
plt.title('hist_normal_Z0')
plt.savefig('hist_normal_Z0')

plt.figure(figsize=(7, 7), dpi=80)
histogram(list_zerada2,m)
plt.title('hist_normal_Z1')
plt.savefig('hist_normal_Z1')









