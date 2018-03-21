from EP3_funcoes_principais import *

def main():
    r=float(input('r: '))
    n=int(input('n: '))
    lista_usada=listaCordasM1(r,n)
    distribuicaoBorda(r,lista_usada)
    distribuicaoRadial(r,lista_usada)
    distribuicaoArea(r,lista_usada)
    distribuicaoCordas(r, lista_usada)
    pausa=input('Digite um valor e depois Enter para continuar(os gráficos gerados serão sobrescritos pelas próximas funções: ')
    lista_usada=listaCordasM2(r,n)
    distribuicaoBorda(r,lista_usada)
    distribuicaoRadial(r,lista_usada)
    distribuicaoArea(r,lista_usada)
    distribuicaoCordas(r, lista_usada)
    pausa=input('Digite um valor Enter para continuar(os gráficos gerados serão sobrescritos pelas próximas funções: ')
    lista_usada=listaCordasM3(r,n)
    distribuicaoBorda(r,lista_usada)
    distribuicaoRadial(r,lista_usada)
    distribuicaoArea(r,lista_usada)
    distribuicaoCordas(r, lista_usada)

main()
    
     