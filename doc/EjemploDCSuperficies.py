# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:34:34 2020

@author: UJA
"""
from ElevacionDelGrado import *
from math import *
import pylab
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy import *    
from sympy.plotting import plot_parametric
from sympy.plotting import plot3d_parametric_line
import math
#from math import comb
from mpl_toolkits import mplot3d
ax = plt.axes(projection='3d')
u=sym.Symbol('u')
v=sym.Symbol('v')

def deCasSuperficies(matriz):
    n=len(matriz[0])
    for r in range(0,n-1):
        brr=[]
        for i in range(0,n-r-1):
            fila=[]
            for j in range(0,n-r-1):
                brrij= ( ( (1-u)*matriz[i][j]+ u*matriz[i+1][j])*(1-v) ) + ( ( (1-u)*matriz[i][j+1]+ u*matriz[i+1][j+1])*(v) )
                fila.append(brrij)
            brr.append(fila)
        matriz=brr
        #print(matriz)
    return matriz[0][0]

def EleGrado(puntos):
    n=len(puntos)
    nuevos_puntos=[]
    nuevos_puntos.append(puntos[0])
    for j in range(1,n):
        nuevos_puntos.append(puntos[j-1]*(j/n+1)+ puntos[j]*(1-(j/n+1)))
    nuevos_puntos.append(puntos[n-1])
    return nuevos_puntos

def ElevacionGradoU(matriz):
    nuevaMatriz=[]
    for i in range(0,len(matriz)):
        nuevaMatriz.append(EleGrado(matriz[i]))
    return nuevaMatriz
    

valoresx=[[0,1,2],[1,2,3],[0,1,2]]
valoresy=[[0,1,0],[2,3,2],[2,3,2]]
valoresz=[[0,0,1],[1,0,2],[1,1,2]]

expresionx=deCasSuperficies(valoresx)
expresiony=deCasSuperficies(valoresy)
expresionz=deCasSuperficies(valoresz)
u1=np.linspace(0,1,100)
v1=np.linspace(0,1,100)
puntosx=[]
puntosy=[]
puntosz=[]
isoparamx=[]
isoparamy=[]
isoparamz=[]
for i in range(0,u1.size):
    isoparamx.append(expresionx.subs({u:u1[i],v:0.5}))
    isoparamy.append(expresiony.subs({u:u1[i],v:0.5}))
    isoparamz.append(expresionz.subs({u:u1[i],v:0.5}))
    for j in range(0,v1.size):
        puntosx.append(expresionx.subs({u:u1[i],v:v1[j]}))
        puntosy.append(expresiony.subs({u:u1[i],v:v1[j]}))
        puntosz.append(expresionz.subs({u:u1[i],v:v1[j]}))
plt.plot(puntosx,puntosy,puntosz)
plt.plot(isoparamx,isoparamy,isoparamz)
"""
valoresx2=ElevacionGradoU(valoresx)
valoresx3=ElevacionGradoV(valoresx2)
valoresy2=ElevacionGradoU(valoresy)
valoresy3=ElevacionGradoV(valoresy2)
valoresz2=ElevacionGradoU(valoresz)
valoresz3=ElevacionGradoV(valoresz2)

superx=deCasSuperficies(valoresx3)
supery=deCasSuperficies(valoresy3)
superz=deCasSuperficies(valoresz3)
u1=np.linspace(0,1,100)
v1=np.linspace(0,1,100)
cosax=[]
cosay=[]
cosaz=[]
otracosax=[]
otracosay=[]
otracosa=[]
for i in range(0,u1.size):
    for j in range(0,v1.size):
        cosax.append(superx.subs({u:u1[i],v:v1[j]}))
        cosay.append(supery.subs({u:u1[i],v:v1[j]}))
        cosaz.append(superz.subs({u:u1[i],v:v1[j]}))
plt.plot(cosax,cosay,cosaz)

"""