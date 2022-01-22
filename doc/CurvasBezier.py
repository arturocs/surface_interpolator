#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:09:54 2020

@author: abel
"""
from DeCasteljau import deCas
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
t=sym.Symbol('t')
def curvaFuncionDePuntos(grado,puntos):
    npuntos=len(puntos)
    #puntosIntervalo=[]
    y=[]
    if(int(npuntos%(grado+1))!=0):
        print("Es posible que no se puedan generar curvas de grado "+str(grado)+", la última será de grado menor")
    for i in range(0,int(npuntos/grado+1)-1):
        
        if(len(puntos[i*grado:(i+1)*grado +1:1])<grado+1):
            #print("b")
            #lista=puntos[i*grado:(i+1)*grado +1:1]
            #for j in range(len(lista),grado+1):
            #    lista=EleGrado(lista)
            l=puntos[i*grado:(i+1)*grado +1:1]
            lista=l
        else:
            #print("a")
            lista=(puntos[i*grado:(i+1)*grado +1:1])
        print(lista)
        if(lista!=[]):
            DC=deCas(lista)
        
        
        z=np.linspace(i,i+0.99,100)
        for j in range(0,z.size):
            y.append(DC.subs(t,(z[j]-i)))
        #print(y)
    return y

def curvaAPartirDeFuncionParaPLY(izq,der,grado,funcion):
    x=[]
    y=[]
    ancho=der-izq
    
    for i in range(0,grado+1):
        x.append(izq+i*(ancho/grado))
        y.append(funcion(izq+i*(ancho/grado)))
    
    DCx=deCas(x)
    DCy=deCas(y)
    z=np.linspace(0,1,100)
    puntos=[]
    for i in range(0,z.size):
        string = ""
        string+=str(DCx.subs(t,z[i]))
        string+=" "
        string+=str(DCy.subs(t,z[i]))
        string+=" "
        string+=str(0)
        puntos.append(string)
    return puntos  
def curvaAPartirDeFuncion(izq,der,grado,funcion):
    x=[]
    y=[]
    if not izq < der:
        print("mala definición de intervalo")
    ancho=der-izq
    for i in range(0,grado+1):
        x.append(izq+i*(ancho/grado))
        y.append(funcion(izq+i*(ancho/grado)))
    
    DCx=deCas(x)
    DCy=deCas(y)
    z=np.linspace(0,1,100)

    plotx=[]
    ploty=[]
    for i in range(0,z.size):
        plotx.append(DCx.subs(t,z[i]))
        ploty.append(DCy.subs(t,z[i]))
    plt.plot(plotx,ploty)  
def fun(x):
    return x**9
curvaAPartirDeFuncion(-2, 2, 9, fun)