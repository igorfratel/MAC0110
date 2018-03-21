#.n Igor Fratel Santana
#.u 9793565

import matplotlib.pyplot as plt
import numpy as np


#funções da seção 3:
def leEntrada(nome):
    lista=[]
    f=open(nome)
    #verificar se a linha contem Q ou H:
    letra=f.readline()
    if letra=='Q\n':
        retorno=0
    if  letra=='H\n':
        retorno=1
    #salvar as coordenadas em uma lista:    
    for line in f:
        if line!='\n':
            y=int(line.split(",")[0])
            x=int(line.split(",")[1])
            lista.append([y,x])
    f.close()
    return retorno,lista

def simulaQuad(n,m,lista,t):
    lista2=[]
    cont=0
    for i in range(t):
        for y in range(n):
            for x in range(m):
                cont=0
                #verificar quantos dos 8 vizinhos estão vivos
                for z in range(y-1,y+2):
                    for w in range (x-1,x+2):
                        if (z%n!=y or w%m!=x) and [z%n,w%m] in lista:
                            cont+=1

                #verificar se a celula está viva e tomar a decisao pertinente baseado no valor de cont:
                if [y,x] in lista:
                    if cont==2 or cont==3:
                        lista2.append([y,x])

                elif cont==3:
                    lista2.append([y,x])
        lista=lista2
        lista2=[]
    return lista

def simulaHex(n,m,lista,t):
    lista2=[]
    cont=0
    #fazer a coluna "invisivel" para o caso de m ímpar
    if (m%2!=0):
        lista.append([x,m] for x in range(n))
    for i in range(t):
        for y in range(n):
            #ele nao vai simular na coluna invisivel, mas as celulas "visiveis" usarão os vizinhos dessa coluna
            for x in range(m):
                cont=0
                #verificar quantos dos 6 vizinhos estão vivos
                if (x%2==0):
                    for z in [[(y-1)%n,x],[y,(x+1)%m],[(y+1)%n,x],[y,(x-1)%m],[(y+1)%n,(x+1)%m],[(y+1)%n,(x-1)%m]]:
                        if z in lista:
                            cont+=1
                else:
                    for w in [[(y-1)%n,x],[y,(x+1)%m],[(y+1)%n,x],[y,(x-1)%m],[(y-1)%n,(x-1)%m],[(y-1)%n,(x+1)%m]]:
                        if w in lista:
                            cont+=1
                #verificar se a celula está viva e tomar a decisao pertinente baseado no valor de cont:
                if [y,x] in lista:
                    if cont==2:
                        lista2.append([y,x])

                else:
                    if cont==3 or cont==5:
                        lista2.append([y,x])
        lista=lista2
        lista2=[]
    return lista

def desenhaQuad(n,m,lista,figura):
    #criar uma matriz zerada nxm de uma forma que o plt.matshow saiba ler
    grade=[[0]*m for i in range(n)]
    #para cada coordenada da lista recebida, substituir na grade por 1: 
    for x in lista:
        grade[x[0]][x[1]]=1
    #funções que exibem a grade
    plt.title("Conway's Game of Life")
    plt.matshow(grade,origin="lower",cmap=plt.get_cmap('summer'),extent=[0, n, 0, m])
    plt.xticks(np.arange(0,m,1))
    plt.yticks(np.arange(0,n,1))
    plt.grid(ls='solid')
    plt.savefig(figura+".png")

def desenhaHex(n,m,lista,figura):   
    import matplotlib.pyplot as plt
    import numpy as np
    from numpy import pi
    from matplotlib.patches import RegularPolygon
    #define o raio e o apotema dos hexagonos
    raio=5
    apotema=(raio*3**(1/2))/2
    #define as dimensoes do grafico
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111,xlim=(0,m*raio*1.5 + raio),ylim=(0,n*apotema*2 + 2*apotema),aspect="equal")
    #plota o hexagono em verde se for vivo e em cinza se for morto 
    for y in range(n):
        for x in range(m):
            centro= (x*1.5*raio+raio,2*apotema*y +2*apotema if x%2==0 else 2*apotema*y + apotema)
            if [y,x] in lista:  
                hexagono=RegularPolygon(centro,6,raio,orientation=pi/6,facecolor="green")
                ax.add_patch(hexagono)
            else:    
                hexagono=RegularPolygon(centro,6,raio,orientation=pi/6,facecolor="gray")
                ax.add_patch(hexagono)
    plt.title("Conway's Game of Life")
    plt.savefig(figura+".png")

def simulaQuadGenerica(n,m,lista,t,b,s):
    lista2=[]
    cont=0
    for i in range(t):
        for y in range(n):
            for x in range(m):
                cont=0
                #verificar quantos dos 8 vizinhos estão vivos
                for z in range(y-1,y+2):
                    for w in range (x-1,x+2):
                        if (z%n!=y or w%m!=x) and [z%n,w%m] in lista:
                            cont+=1

                #verificar se a celula está viva e tomar a decisao pertinente baseado no valor de cont:
                if [y,x] in lista:
                    if cont==s:
                        lista2.append([y,x])

                elif cont==b:
                    lista2.append([y,x])
        lista=lista2
        lista2=[]
    return lista

def simulaHexGenerica(n,m,lista,t,b,s): 
    lista2=[]
    cont=0
    #fazer a coluna "invisivel" para o caso de m ímpar
    if (m%2!=0):
        lista.append([x,m] for x in range(n))
    for i in range(t):
        for y in range(n):
            for x in range(m):
                cont=0
                #verificar quantos dos 6 vizinhos estão vivos
                if (x%2==0):
                    for z in [[(y-1)%n,x],[y,(x+1)%m],[(y+1)%n,x],[y,(x-1)%m],[(y+1)%n,(x+1)%m],[(y+1)%n,(x-1)%m]]:
                        if z in lista:
                            cont+=1
                else:
                    for w in [[(y-1)%n,x],[y,(x+1)%m],[(y+1)%n,x],[y,(x-1)%m],[(y-1)%n,(x-1)%m],[(y-1)%n,(x+1)%m]]:
                        if w in lista:
                            cont+=1
                #verificar se a celula está viva e tomar a decisao pertinente baseado no valor de cont:
                if [y,x] in lista:
                    if cont==s:
                        lista2.append([y,x])

                else:
                    if cont==b:
                        lista2.append([y,x])
        lista=lista2
        lista2=[]
    return lista

def haRepeticoes(n,m,lista,t):
    lista2=[]
    rpt=[]
    rpt.append(lista)
    cont=0
    rpt_cont=0
    for i in range(t):
        for y in range(n):
            for x in range(m):
                cont=0
                #verificar quantos dos 8 vizinhos estão vivos
                for z in range(y-1,y+2):
                    for w in range (x-1,x+2):
                        if (z%n!=y or w%m!=x) and [z%n,w%m] in lista:
                            cont+=1

                #verificar se a celula está viva e tomar a decisao pertinente baseado no valor de cont:
                if [y,x] in lista:
                    if cont==2 or cont==3:
                        lista2.append([y,x])

                else:
                    if cont==3:
                        lista2.append([y,x])
        lista=lista2
        lista2=[]
        rpt.append(lista)
    #a lista rpt guardou cada estado de jogo e agora ela compara seus elementos para encontrar duplicatas
    for i in range(len(rpt)-1):
        for j in range(i+1,len(rpt)):
            if (len(rpt[i])==len(rpt[j])) and (all(x in rpt[i] for x in rpt[j])):
                rpt_cont+=1
        
    if rpt_cont>0:
        return True
    else:
        return False