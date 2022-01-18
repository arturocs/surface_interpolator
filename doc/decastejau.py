# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:11:05 2020
@author: PcCom
"""
from math import *
import pylab
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x=sym.Symbol('x')
def deCas(puntos):
    n=len(puntos)
    
   
    for j in range(1,n):
        nueva=[]
        for i in range(1,n-j+1):
            nueva.append(puntos[i-1]*(1-x)+puntos[i]*x)
           
        puntos=nueva
    
    return puntos[0] 

def parte(m,n,vector):
    long=len(vector)
    trozo=[]
    for i in range(0,n):
        if(i+m<long):
            trozo.append(vector(i))
        else:
            trozo.append(vector(n-i))
        


def curvaFuncionDePuntos(grado,puntos):
    npuntos=len(puntos)
    #puntosIntervalo=[]
    y=[]
    for i in range(0,int(npuntos/grado+1)-1):
        #print(puntos[i*grado:(i+1)*grado +1:1])
        #puntosIntervalo.append(puntos[i*grado:(i+1)*grado +1:1])
        
        if(len(puntos[i*grado:(i+1)*grado +1:1])<grado+1):
            l=puntos[i*grado:(i+1)*grado +1:1]
            l=l+(puntos[0:grado+1-len(puntos[i*grado:(i+1)*grado +1:1]):1])
            lista=l
        else:
            lista=(puntos[i*grado:(i+1)*grado +1:1])
        print(lista)
        DC=deCas(lista)
        
        
        z=np.linspace(i,i+0.99,100)
        for j in range(0,z.size):
            y.append(DC.subs(x,(z[j]-i)))
    z=np.linspace(0,int(npuntos/grado),100*int((npuntos/grado+1)-1))
    plt.plot(z,y)
    
puntos=[4,3,5,8,11,5,4,3,9,13,17,22]
#print(puntos[0:3:1])
curvaFuncionDePuntos(3,puntos)
"""
puntos1=[4,3,5,8]
puntos2=[8,5,6,4]
DC1=deCas(puntos1)
DC2=deCas(puntos2)
#print(DC)
z1=np.linspace(0.0,0.99,100)
z2=np.linspace(1.0,2.0,100)
y=[]
z=np.linspace(0.0,2.0,200)
for i in range(0,z1.size):
    y.append(DC1.subs(x,z1[i]))
for i in range(0,z2.size):
    #print(z[i]-1)
    y.append(DC2.subs(x,(z2[i]-1)/(2-1)))#(z[i]-u_i)/(u_i+1 - u_i)
plt.plot(z,y)
"""