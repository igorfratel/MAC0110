#.n Igor Fratel Santana
#.u 9793565
import matplotlib.pyplot as plt
import numpy as np
from math import pi,sin,cos
from EP3_modif_ep2_e_auxiliares import *

def distribuicaoBorda(r,listaCordas):
    tupla=()
    lista=[[],[],[],[],[],[],[],[]]
    lista_hist=[None]*8
    i=0
    #verificar em qual pedaço do circulo está o ponto:
    while i<len(listaCordas):
        if cos(2*pi)*r>listaCordas[i][0][0]>=cos(pi/4)*r and sin(2*pi)*r<listaCordas[i][0][1]<=sin(pi/4)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[0].append(tupla)
        elif cos(pi/4)*r>listaCordas[i][0][0]>=cos(pi/2)*r and sin(pi/4)*r<listaCordas[i][0][1]<=sin(pi/2)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[1].append(tupla)
        elif cos(pi/2)*r>listaCordas[i][0][0]>=cos(3*pi/4)*r and sin(pi/2)*r>listaCordas[i][0][1]>=sin(3*pi/4)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[2].append(tupla)
        elif cos(3*pi/4)*r>listaCordas[i][0][0]>=cos(pi)*r and sin(3*pi/4)*r>listaCordas[i][0][1]>=sin(pi)*r :
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[3].append(tupla)
        elif cos(pi)*r<listaCordas[i][0][0]<=cos(5*pi/4)*r and sin(pi)*r>listaCordas[i][0][1]>=sin(5*pi/4)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[4].append(tupla)
        elif cos(5*pi/4)*r<listaCordas[i][0][0]<=cos(3*pi/2)*r and sin(5*pi/4)*r>listaCordas[i][0][1]>=sin(3*pi/2)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[5].append(tupla)
        elif cos(3*pi/2)*r<listaCordas[i][0][0]<=cos(7*pi/4)*r and sin(3*pi/2)*r<listaCordas[i][0][1]<=sin(7*pi/4)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[6].append(tupla)
        elif cos(7*pi/4)*r<listaCordas[i][0][0]<=cos(2*pi)*r and sin(7*pi/4)*r<listaCordas[i][0][1]<=sin(2*pi)*r:
            tupla=(listaCordas[i][0][0],listaCordas[i][0][1])
            lista[7].append(tupla)

        if cos(2*pi)*r>listaCordas[i][1][0]>=cos(pi/4)*r and sin(2*pi)*r<listaCordas[i][1][1]<=sin(pi/4)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[0].append(tupla)
        elif cos(pi/4)*r>listaCordas[i][1][0]>=cos(pi/2)*r and sin(pi/4)*r<listaCordas[i][1][1]<=sin(pi/2)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[1].append(tupla)
        elif cos(pi/2)*r>listaCordas[i][1][0]>=cos(3*pi/4)*r and sin(pi/2)*r>listaCordas[i][1][1]>=sin(3*pi/4)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[2].append(tupla)
        elif cos(3*pi/4)*r>listaCordas[i][1][0]>=cos(pi)*r and sin(3*pi/4)*r>listaCordas[i][1][1]>=sin(pi)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[3].append(tupla)
        elif cos(pi)*r<listaCordas[i][1][0]<=cos(5*pi/4)*r and sin(pi)*r>listaCordas[i][1][1]>=sin(5*pi/4)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[4].append(tupla)
        elif cos(5*pi/4)*r<listaCordas[i][1][0]<=cos(3*pi/2)*r and sin(5*pi/4)*r>listaCordas[i][1][1]>=sin(3*pi/2)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[5].append(tupla)
        elif cos(3*pi/2)*r<listaCordas[i][1][0]<=cos(7*pi/4)*r and sin(3*pi/2)*r<listaCordas[i][1][1]<=sin(7*pi/4)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[6].append(tupla)
        elif cos(7*pi/4)*r<listaCordas[i][1][0]<=cos(2*pi)*r and sin(7*pi/4)*r<listaCordas[i][1][1]<=sin(2*pi)*r:
            tupla=(listaCordas[i][1][0],listaCordas[i][1][1])
            lista[7].append(tupla)
        i+=1 

    plt.figure(figsize=(15, 6), dpi=80)
    plt.subplot(121)
    thetas=np.arange(0,2*np.pi,0.01)
    plt.plot(r*np.cos(thetas), r*np.sin(thetas), 'b-')
    #plotando de acordo com a categoria
    i=0
    while i<8:
        j=0
        while j<len(lista[i]):
            if i==0:
                plt.plot(lista[i][j][0],lista[i][j][1],"ro")
            elif i==1:
                plt.plot(lista[i][j][0],lista[i][j][1],"bo")
            elif i==2:
                plt.plot(lista[i][j][0],lista[i][j][1],"mo")
            elif i==3:
                plt.plot(lista[i][j][0],lista[i][j][1],"ko")
            elif i==4:
                plt.plot(lista[i][j][0],lista[i][j][1],"go")
            elif i==5:
                plt.plot(lista[i][j][0],lista[i][j][1],"yo")
            elif i==6:
                plt.plot(lista[i][j][0],lista[i][j][1],"wo")
            elif i==7:
                plt.plot(lista[i][j][0],lista[i][j][1],"co")
            j+=1
        i+=1


    cores=['r','b','m','k','g','y','w','c']
    plt.subplot(122)
    i=0
    while i<8:
        lista_hist[i]=len(lista[i])
        i+=1
    x=np.arange(8)
    plt.bar(x,lista_hist,color=cores)
    plt.title('distribuicao_borda')
    plt.savefig('distribuicao_borda.png')

 
def distribuicaoRadial(r,listaCordas):
    listamedia=determinaPontosMedios(listaCordas)
    tupla=()
    lista=[[],[],[],[],[],[],[],[]]
    lista_hist=[None]*8
    i=0
    while i<len(listamedia):
        if listamedia[i][0]**2 + listamedia[i][1]**2<=(r/8)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[0].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=(r/4)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[1].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=(3*r/8)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[2].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=(r/2)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[3].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=(5*r/8)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[4].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=(3*r/4)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[5].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=(7*r/8)**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[6].append(tupla)
        elif listamedia[i][0]**2 + listamedia[i][1]**2<=r**2:
            tupla=(listamedia[i][0],listamedia[i][1])
            lista[7].append(tupla)
        i+=1

    plt.figure(figsize=(15, 6), dpi=80)
    plt.subplot(121)
    thetas=np.arange(0,2*np.pi,0.01)
    plt.plot(r*np.cos(thetas), r*np.sin(thetas), 'b-')

    i=0
    while i<8:
        j=0
        while j<len(lista[i]):
            if i==0:
                plt.plot(lista[i][j][0],lista[i][j][1],"ro")
            elif i==1:
                plt.plot(lista[i][j][0],lista[i][j][1],"bo")
            elif i==2:
                plt.plot(lista[i][j][0],lista[i][j][1],"mo")
            elif i==3:
                plt.plot(lista[i][j][0],lista[i][j][1],"ko")
            elif i==4:
                plt.plot(lista[i][j][0],lista[i][j][1],"go")
            elif i==5:
                plt.plot(lista[i][j][0],lista[i][j][1],"yo")
            elif i==6:
                plt.plot(lista[i][j][0],lista[i][j][1],"wo")
            elif i==7:
                plt.plot(lista[i][j][0],lista[i][j][1],"co")
            j+=1
        i+=1

    cores=['r','b','m','k','g','y','w','c']
    plt.subplot(122)
    i=0
    while i<8:
        lista_hist[i]=len(lista[i])
        i+=1
    x=np.arange(8)
    plt.bar(x,lista_hist,color=cores)
    plt.title('distribuicaoRadial')
    plt.savefig('distribuicaoRadial.png')


def distribuicaoArea(r,listaCordas):
    listamedia=determinaPontosMedios(listaCordas)
    tupla=()
    lista=[[],[],[],[],[],[],[],[]]
    lista_hist=[None]*8
    i=0
    while i<len(listamedia):
        if listamedia[i][1]>=0:
            if (listamedia[i][0]-(-7*r/8))**2 + listamedia[i][1]**2 <=(r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[0].append(tupla)
            elif (listamedia[i][0]-(-3*r/4))**2 + listamedia[i][1]**2 <=(2*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[1].append(tupla)
            elif (listamedia[i][0]-(-5*r/8))**2 + listamedia[i][1]**2 <=(3*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[2].append(tupla)
            elif (listamedia[i][0]-(-4*r/8))**2 + listamedia[i][1]**2 <=(4*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[3].append(tupla)
            elif (listamedia[i][0]-(-3*r/8))**2 + listamedia[i][1]**2 <=(5*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[4].append(tupla)
            elif (listamedia[i][0]-(-2*r/8))**2 + listamedia[i][1]**2 <=(6*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[5].append(tupla)
            elif (listamedia[i][0]-(-r/8))**2 + listamedia[i][1]**2 <=(7*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[6].append(tupla)
            elif (listamedia[i][0])**2 + listamedia[i][1]**2 <=(8*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[7].append(tupla)

        if listamedia[i][1]<0:
            if (listamedia[i][0]-(7*r/8))**2 + listamedia[i][1]**2 <=(r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[7].append(tupla)
            elif (listamedia[i][0]-(3*r/4))**2 + listamedia[i][1]**2 <=(2*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[6].append(tupla)
            elif (listamedia[i][0]-(5*r/8))**2 + listamedia[i][1]**2 <=(3*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[5].append(tupla)
            elif (listamedia[i][0]-(4*r/8))**2 + listamedia[i][1]**2 <=(4*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[4].append(tupla)
            elif (listamedia[i][0]-(3*r/8))**2 + listamedia[i][1]**2 <=(5*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[3].append(tupla)
            elif (listamedia[i][0]-(2*r/8))**2 + listamedia[i][1]**2 <=(6*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[2].append(tupla)
            elif (listamedia[i][0]-(r/8))**2 + listamedia[i][1]**2 <=(7*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[1].append(tupla)
            elif (listamedia[i][0])**2 + listamedia[i][1]**2 <=(8*r/8)**2:
                tupla=(listamedia[i][0],listamedia[i][1])
                lista[0].append(tupla)
        i+=1

    plt.figure(figsize=(15, 6), dpi=80)
    plt.subplot(121)
    thetas=np.arange(0,2*np.pi,0.01)
    plt.plot(r*np.cos(thetas), r*np.sin(thetas), 'b-')

    i=0
    while i<8:
        j=0
        while j<len(lista[i]):
            if i==0:
                plt.plot(lista[i][j][0],lista[i][j][1],"ro")
            elif i==1:
                plt.plot(lista[i][j][0],lista[i][j][1],"bo")
            elif i==2:
                plt.plot(lista[i][j][0],lista[i][j][1],"mo")
            elif i==3:
                plt.plot(lista[i][j][0],lista[i][j][1],"ko")
            elif i==4:
                plt.plot(lista[i][j][0],lista[i][j][1],"go")
            elif i==5:
                plt.plot(lista[i][j][0],lista[i][j][1],"yo")
            elif i==6:
                plt.plot(lista[i][j][0],lista[i][j][1],"wo")
            elif i==7:
                plt.plot(lista[i][j][0],lista[i][j][1],"co")
            j+=1
        i+=1

    cores=['r','b','m','k','g','y','w','c']
    plt.subplot(122)
    i=0
    while i<8:
        lista_hist[i]=len(lista[i])
        i+=1
    x=np.arange(8)
    plt.bar(x,lista_hist,color=cores)
    plt.title('distribuicaoArea')
    plt.savefig('distribuicaoArea.png')
    

def distribuicaoCordas(r, listaCordas):
    plt.figure(figsize=(7, 7), dpi=80)
    thetas=np.arange(0,2*np.pi,0.01)
    plt.plot(r*np.cos(thetas), r*np.sin(thetas), 'b-')
    listax=[]
    listay=[]
    for i in listaCordas:
        for j in i:
            listax.append(j[0])
            listay.append(j[1])
    plt.plot(listax,listay)
    plt.title('distribuicaoCordas')
    plt.savefig('distribuicao_cordas.png')
        
    
    