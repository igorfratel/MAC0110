#.n Igor Fratel Santana
#.u 9793565

from random import uniform
from math import pi,sin,sqrt

def main():
    r = float(input("Digite um valor para o raio "))
    n = int(input("Digite um número de vezes para a execução do método "))
    
    def metodo1(r,n):
        i=0
        contador=0
        #calcular a área do triângulo
        L=r*sqrt(3)
        while i<n:
            #Escolher dois pontos entre 0 e ~(2*pi*r) 
            #Imaginar a circunferencia como uma reta esticada
            A=uniform(0,(2*pi*r))
            B=uniform(0,(2*pi*r))
            #garantir que o valor do arco é positivo            
            if A-B<0:
                A,B=B,A
            #calcular o ângulo formado entre os pontos A e B
            angulo_central=(2*pi*(A-B))/(2*pi*r)
            #calcular a corda AB
            AB=2*r*sin(angulo_central/2)
            if AB>L:
                contador+=1
            i+=1
        return contador/n
    
    def metodo2(r,n):
        i=0
        contador=0
        while i<n:
            #Escolher um ponto C na circunferencia e depois um ponto P em OC
            #é a mesma coisa que escolher um ponto P no raio. 
            #Escolher um ponto entre 0 e ~r
            P=uniform(0,r) 
            #P é a distância entre um ponto no raio e a origem 
            if P<r/2:
                contador+=1
            i+=1
        return contador/n
    
    def metodo3(r,n):
        i=0
        contador=0
        while i<n:
            #Pelo axioma da escolha, sabemos que o produto cartesiano de R(o plano cartesiano)
            #possui a mesma cardinalidade que o próprio conjunto R(a reta real).
        
            #Referência: http://math.stackexchange.com/questions/180671/cardinality-of-cartesian-square
        
            #Portanto eu interpretei a área do círculo como uma reta de pi*r*r de comprimento.
            #Consequentemente, a área do "círculo menor" inscrito no triãngulo será uma reta com
            #1/4 do comprimento da reta pi*r*r.         
            #A ideia do "círculo menor" vem da especificação do "random midpoint method" e da Figura 3 do EP
            P=uniform(0,pi*r*r)
            if P<pi*r*r/4:
                contador+=1
            i+=1
        return contador/n
    
    print("Método 1: ", metodo1(r,n))
    print("Método 2: ", metodo2(r,n))
    print("Método 3: ", metodo3(r,n))
  
main()
    
