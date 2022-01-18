# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:05:52 2020

@author: PcCom
"""
import numpy as np
import sympy as sym
import math
import matplotlib.pyplot as plt
t=sym.Symbol('t')

def fun(x):
    return (math.cos(x)-x*math.sin(x))

def interpolanteCuadraticoC1(izq,der,long,f):
    if(izq>=der):
        print("izquierda debe ser menor que derecha")
        return False
    base=[(1-t)**2,2*(1-t)*t,t**2]
    polinomios=[]
    #marca el comienzo del intervalo actual
    intervaloActual=izq
    i=0
    x=[]
    y=[]
    while intervaloActual<der:
        
        if (intervaloActual+long <der):
            vi=intervaloActual
            wi=intervaloActual + long*0.5
            vI=intervaloActual+long
        else:
            vi=intervaloActual
            vI=der
            wi=intervaloActual+(vI-vi)*0.5
        cvi=-(1/4)*f((i-1)*long) + f((i-0.5)*long) - 0.5*f(i*long) +f((i+0.5)*long)-(1/4)*f((i+1)*long)
        cwi=-0.5*f(i*long)+2*f((i+0.5)*long)-0.5*f((i+1)*long)
        cvI=-(1/4)*f((i)*long)+f((i+1-0.5)*long)- 0.5*f((i+1)*long)+f((i+1+0.5)*long)-(1/4)*f((i+1+1)*long)
        polinomio=cvi*base[0]+cwi*base[1]+cvI*base[2]
        #print(cvi)
        #print(cwi)
        #print(cvI)
        z=np.linspace(vi,vI,10)
        for j in range(0,z.size):
            #print((z[j]-i*long)/long)
            x.append(z[j])
            y.append(polinomio.subs(t,(z[j]-i*long)/long))
        i=i+1
        intervaloActual=intervaloActual+long
    plt.plot(x,y)

def interpolanteCubicoC2(izq,der,long,f):
    if(izq>=der):
        print("izquierda debe ser menor que derecha")
        return False
    base=[(1-t)**3,3*t*(1-t)**2,3*(1-t)*t**2,t**3]
    polinomios=[]
    #marca el comienzo del intervalo actual
    intervaloActual=izq
    i=0
    x=[]
    y=[]
    while intervaloActual<der:
        if (intervaloActual+long <der):
            ui=intervaloActual-long
            vi=intervaloActual
            wi=intervaloActual + long*0.5
            vI=intervaloActual+long
        else:
            vi=intervaloActual
            vI=der
            wi=intervaloActual+(vI-vi)*0.5
        cvi=-(1/36)*f((i-2)*long)+(1/9)*f((i-1)*long)+(6/5)*f(i*long)+(1/9)*f((i+1)*long)-(1/36)*f((i+2)*long)
        cwi=-(1/9)*f((i-1)*long) +(6/5)*f(i*long)+(1/3)*f((i+1)*long)-(1/18)*f((i+2)*long)
        cvI=-(1/36)*f((i-1)*long)+(1/9)*f((i)*long)+(6/5)*f((i+1)*long)+(1/9)*f((i+2)*long)-(1/36)*f((i+3)*long)
        cui=-(1/18)*f((i-1*long)) +(1/3)*f(i*long)+(6/5)*f((i+1)*long)-(1/9)*f((i+2)*long)
        polinomio=cvi*base[0]+cwi*base[1]+cwi*base[2]+cvI*base[3]
        #print(cvi)
        #print(cwi)
        #print(cvI)
        z=np.linspace(vi,vI,10)
        for j in range(0,z.size):
                #print((z[j]-i*long)/long)
            x.append(z[j])
            y.append(polinomio.subs(t,(z[j]-i*long)/long))
        i=i+1
        intervaloActual=intervaloActual+long
    plt.plot(x,y)
    
def interpolanteCuadraticoC12(izq,der,long,f):
    if(izq>=der):
        print("izquierda debe ser menor que derecha")
        return False
    base=[(1-t)**2,2*(1-t)*t,t**2]
    polinomios=[]
    #marca el comienzo del intervalo actual
    intervaloActual=izq
    i=0
    magenta=True
    while intervaloActual<der:
        
        if (intervaloActual+long <der):
            vi=intervaloActual
            wi=intervaloActual + long*0.5
            vI=intervaloActual+long
        else:
            vi=intervaloActual
            vI=der
            wi=intervaloActual+(vI-vi)*0.5
        cvi=-(1/4)*f((i-1)*long) + f((i-0.5)*long) - 0.5*f(i*long) +f((i+0.5)*long)-(1/4)*f((i+1)*long)
        cwi=-0.5*f(i*long)+2*f((i+0.5)*long)-0.5*f((i+1)*long)
        cvI=-(1/4)*f((i)*long)+f((i+1-0.5)*long)- 0.5*f((i+1)*long)+f((i+1+0.5)*long)-(1/4)*f((i+1+1)*long)
        polinomio=cvi*base[0]+cwi*base[1]+cvI*base[2]
        
        x=[]
        y=[]
        z=np.linspace(vi,vI,10)
        for j in range(0,z.size):
            #print((z[j]-i*long)/long)
            x.append(z[j])
            y.append(polinomio.subs(t,(z[j]-i*long)/long))
        #print(magenta)
        if (magenta==True):
            plt.plot(x,y,color='black')
            magenta=False
        else:
            plt.plot(x,y,'r')
            magenta=True
        
        i=i+1
        intervaloActual=intervaloActual+long
def interpolanteCubicoC22(izq,der,long,f):
    if(izq>=der):
        print("izquierda debe ser menor que derecha")
        return False
    base=[(1-t)**3,3*t*(1-t)**2,3*(1-t)*t**2,t**3]
    polinomios=[]
    #marca el comienzo del intervalo actual
    intervaloActual=izq
    i=0
    x=[]
    y=[]
    while intervaloActual<der:
        if (intervaloActual+long <der):
            ui=intervaloActual-long
            vi=intervaloActual
            wi=intervaloActual + long*0.5
            vI=intervaloActual+long
        else:
            vi=intervaloActual
            vI=der
            wi=intervaloActual+(vI-vi)*0.5
        cvi=-(8/15)*f((i-0.5)*long)+(2/5)*f((i)*long)+(4/15)*f((i+0.5)*long)+-(1/5)*f((i+1)*long)
        cwi=-(1/5)*f((i-1)*long) +(4/15)*f((i-0.5)*long)+(2/5)*f((i)*long)-(8/15)*f((i+0.5)*long)
        cvI=-(8/15)*f((i+0.5)*long)+(2/5)*f((i+1)*long)+(4/15)*f((i+1.5)*long)+-(1/5)*f((i+2)*long)
        cui=-(1/10)*f((i-1)*long)+(2/5)*f((i-0.5)*long)+(2/5)*f(i*long)+(2/5)*f((i+0.5)*long)-(1/10)*f((i+1)*long)
        polinomio=cvi*base[0]+cwi*base[1]+cwi*base[2]+cvI*base[3]
        #print(cvi)
        #print(cwi)
        #print(cvI)
        z=np.linspace(vi,vI,10)
        for j in range(0,z.size):
                #print((z[j]-i*long)/long)
            x.append(z[j])
            y.append(polinomio.subs(t,(z[j]-i*long)/long))
        i=i+1
        intervaloActual=intervaloActual+long
    plt.plot(x,y)        
"""   
print(fun(0))
z=np.linspace(0,2,200)
x1=[]
y1=[]
for j in range(0,z.size):
    
    x1.append(z[j])
    y1.append(fun(z[j]))
plt.plot(x1,y1)
"""
#interpolanteCuadraticoC1(0,2,0.1,fun)
#interpolanteCubicoC2(0,2,0.01,fun)
interpolanteCuadraticoC12(0,2,0.1,fun)
interpolanteCubicoC22(0,2,0.01,fun)