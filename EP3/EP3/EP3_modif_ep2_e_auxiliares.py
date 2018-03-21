#.n Igor Fratel Santana
#.u 9793565

from random import random,uniform
from math import pi,sin,sqrt,cos,log

#funções para auxiliar as modificações no ep2:
def determinaPontosMedios(listaExtremos):
    i=0
    lista=[]
    tupla=()
    xM,yM=0,0
    while i<len(listaExtremos):
        xM=(listaExtremos[i][0][0]+listaExtremos[i][1][0])/2
        yM=(listaExtremos[i][0][1]+listaExtremos[i][1][1])/2
        tupla=(xM,yM)
        lista.append(tupla)
        i+=1
    return lista
    
def determinaPontosExtremos(r,listaPontosMedios):
    d=0
    i=0
    seno=0
    coseno=0
    xA,xB,yA,yB=0,0,0,0
    xC,yC=0,0
    lista=[]
    tupla=()
    while i<len(listaPontosMedios):
        d=(listaPontosMedios[i][0]**2 + listaPontosMedios[i][1]**2)**(1/2) 
        coseno=d/r
        seno=(1-coseno**2)**(1/2)
        xC=listaPontosMedios[i][0]*r/d
        yC=listaPontosMedios[i][1]*r/d
        xA = coseno*xC + (-seno*yC)
        yA = seno*xC + coseno*yC
        xB = coseno*xC + seno*yC
        yB = -seno*xC + coseno*yC
        tupla = ((xA,yA),(xB,yB))
        lista.append(tupla)
        i+=1
    return lista

 
 
#Funções modificadas do EP2:
 
def listaCordasM1(r,n):
    xA,xB,yA,yB = 0,0,0,0
    i=0
    lista=[]
    tupla=()
    while i<n:
        #Escolher dois pontos entre 0 e ~(2*pi*r) 
        #Imaginar a circunferencia como uma reta esticada
        A=uniform(0,(2*pi*r))
        B=uniform(0,(2*pi*r))
        #calcular as coordenadas de A e B:
        #calcular os angulos centrais de A e B, sabendo o comprimento dos arcos:
        ang_A = A/r
        ang_B = B/r
        #calcular os X's:
        xA = cos(ang_A)*r
        xB = cos(ang_B)*r
        #calcular os Y's:
        yA = sin(ang_A)*r
        yB = sin(ang_B)*r
        tupla=((xA,yA),(xB,yB))
        lista.append(tupla)
        i+=1
    return lista
 
def listaCordasM2(r,n):
        i=0
        C,xC,yC,ang_C=0,0,0,0
        xP,yP=0,0
        lista=[]
        tupla=()
        while i<n:
            #Escolher um ponto C na circunferencia
            C=uniform(0,2*pi*r)
            ang_C= C/r
            xC=cos(ang_C)*r
            yC=sin(ang_C)*r
            #escolher um ponto P na reta OC
            xP=uniform(0,xC)
            yP=(yC/xC)*(xP-xC)+yC
            tupla=(xP,yP)
            lista.append(tupla)
            i+=1
        return determinaPontosExtremos(r,lista)
        
        
        
        
def listaCordasM3(r,n):
        i=0
        lista=[]
        tupla=()
        while i<n:
            #Escolher um ponto P no círculo que será o ponto médio da corda
            xP=uniform(-r,r)
            yP=uniform(-r,r)
            #ver se o ponto está mesmo no círculo
            while xP**2+yP**2>r**2:
                xP=uniform(0,r)
                yP=uniform(0,r)
            tupla=(xP,yP)
            lista.append(tupla)
            i+=1
        #retorna os pontos extremos da corda com P sendo o ponto médio
        return determinaPontosExtremos(r,lista)
        

        