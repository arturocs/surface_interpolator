#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:26:25 2020

@author: abel
"""
from math import comb
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
t=sym.Symbol('t')
def B_jn(j,n):
    return comb(n,j)*(t**j)*(1-t)**(n-j)




def curvaBezierBaseBernstein(coordenadax,coordenaday):
    if(len(coordenadax)!=len(coordenaday)):
        print("No es posible calcular la curva, revise los puntos")
        print("ambas listas han de tener el mismo numero de puntos")
    grado = len(coordenadax)
    BaseBernstein=[]
    for i in range(0,grado):
        BaseBernstein.append(B_jn(i,grado-1))
    coordenadaxEnBase=0
    coordenadayEnBase=0
    for i in range(0,grado):
        coordenadaxEnBase+=coordenadax[i]*BaseBernstein[i]
        coordenadayEnBase+=coordenaday[i]*BaseBernstein[i]
    z=np.linspace(0,1,100)
    x=[]
    y=[]
    for i in range(0,z.size):
        x.append(coordenadaxEnBase.subs(t,z[i]))
        y.append(coordenadayEnBase.subs(t,z[i]))
    plt.plot(x,y)
coordenadax=[0,1,-1,3]
coordenaday=[1,2,-3,0]
curvaBezierBaseBernstein(coordenadax, coordenaday)