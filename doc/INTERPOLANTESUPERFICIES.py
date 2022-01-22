# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:21:50 2020

@author: PcCom
"""
from math import exp
from math import floor
from math import factorial
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
ind=[[4,0,0],[3,1,0],[3,0,1],[2,2,0],[2,1,1],[2,0,2],[1,3,0],[1,2,1],[1,1,2],[1,0,3],[0,4,0],[0,3,1],[0,2,2],[0,1,3],[0,0,4]]
def funcion(x):
    return 0.75*exp(-((9*x[0]-2)**2)/4 - ((9*x[1]-2)**2)/4)+ 0.75*exp(-((9*x[0]+1)**2)/49 - ((9*x[1]+1)**2)/10)+ 0.5*exp(-((9*x[0]-7)**2)/4 - ((9*x[1]-3)**2)/4)-0.2*exp(-((9*x[0]-4)**2) - ((9*x[1]-7)**2))
def RotateRight(lista,n):
    nueva=[]
    for i in range(len(lista)-n,len(lista)):
        nueva.append(lista[i])
    for i in range(0,len(lista)-n):
        nueva.append(lista[i])
    return nueva
def Flatten(matrix):
    nueva=[]
    for i in range(0,len(matrix)):
        nueva+=matrix[i]
    return nueva
def Dot(l1,l2):
    producto=0
    for i in range(0,len(l1)):
        producto+=l1[i]*l2[i]
    return producto
#DEFINIMOS CADA UNO DE LOS COEFICIENTES
#COMPONENTE A COMPONENTE PARA QUE SEA MAS CLARO Y FACIL DE TRABAJAR
#AUNQUE MAS TEDIOSO DE ESCRIBIR
def Vij(i,j,h):
    return [i*h+j*h,i*h-j*h]
def uij11(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j+1,h)
    return [(3*vij[0]+vij1[0])/4,(3*vij[1]+vij1[1])/4 ]
def uij10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j,h)
    return [(3*vij[0]+vij1[0])/4,(3*vij[1]+vij1[1])/4 ]
def uij0menos1(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j-1,h)
    return [(3*vij[0]+vij1[0])/4,(3*vij[1]+vij1[1])/4 ]
def uijmenos1menos1(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i-1,j-1,h)
    return [(3*vij[0]+vij1[0])/4,(3*vij[1]+vij1[1])/4 ]
def uijmenos10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i-1,j,h)
    return [(3*vij[0]+vij1[0])/4,(3*vij[1]+vij1[1])/4 ]
def uij01(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j+1,h)
    return [(3*vij[0]+vij1[0])/4,(3*vij[1]+vij1[1])/4 ]
def eij10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j,h)
    return [(vij[0]+vij1[0])/2,(vij[1]+vij1[1])/2 ]
def eij01(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j+1,h)
    return [(vij[0]+vij1[0])/2,(vij[1]+vij1[1])/2 ]
def eij11(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j+1,h)
    return [(vij[0]+vij1[0])/2,(vij[1]+vij1[1])/2 ]
def zij11(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j+1,h)
    vij2=Vij(i+1,j,h)
    return [(2*vij[0]+vij1[0]+vij2[0])/4,(2*vij[1]+vij1[1]+vij2[1])/4 ]
def zij10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j,h)
    vij2=Vij(i,j-1,h)
    return [(2*vij[0]+vij1[0]+vij2[0])/4,(2*vij[1]+vij1[1]+vij2[1])/4 ]
def zij0menos1(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j-1,h)
    vij2=Vij(i-1,j-1,h)
    return [(2*vij[0]+vij1[0]+vij2[0])/4,(2*vij[1]+vij1[1]+vij2[1])/4 ]
def zijmenos1menos1(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i-1,j-1,h)
    vij2=Vij(i-1,j,h)
    return [(2*vij[0]+vij1[0]+vij2[0])/4,(2*vij[1]+vij1[1]+vij2[1])/4 ]
def zijmenos10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i-1,j,h)
    vij2=Vij(i,j+1,h)
    return [(2*vij[0]+vij1[0]+vij2[0])/4,(2*vij[1]+vij1[1]+vij2[1])/4 ]
def zij01(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j+1,h)
    vij2=Vij(i+1,j+1,h)
    return [(2*vij[0]+vij1[0]+vij2[0])/4,(2*vij[1]+vij1[1]+vij2[1])/4 ]
def tij(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j+1,h)
    vij2=Vij(i+1,j,h)
    return [(vij[0]+vij1[0]+vij2[0])/3,(vij[1]+vij1[1]+vij2[1])/3 ]
def bij(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j+1,h)
    vij2=Vij(i,j+1,h)
    return [(vij[0]+vij1[0]+vij2[0])/3,(vij[1]+vij1[1]+vij2[1])/3 ]
def wij11(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j+1,h)
    return [(2*vij[0]+vij1[0])/3,(2*vij[1]+vij1[1])/3 ]
def wij10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i+1,j,h)
    return [(2*vij[0]+vij1[0])/3,(2*vij[1]+vij1[1])/3 ]
def wij0menos1(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j-1,h)
    return [(2*vij[0]+vij1[0])/3,(2*vij[1]+vij1[1])/3 ]
def wijmenos1menos1(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i-1,j-1,h)
    return [(2*vij[0]+vij1[0])/3,(2*vij[1]+vij1[1])/3 ]
def wijmenos10(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i-1,j,h)
    return [(2*vij[0]+vij1[0])/3,(2*vij[1]+vij1[1])/3 ]
def wij01(i,j,h):
    vij=Vij(i,j,h)
    vij1=Vij(i,j+1,h)
    return [(2*vij[0]+vij1[0])/3,(2*vij[1]+vij1[1])/3 ]

def D3ijh(i,j,h):
    return [Vij(i,j,h),wij11(i,j,h),wij10(i,j,h),wij0menos1(i,j,h),wijmenos1menos1(i,j,h),wijmenos10(i,j,h),wij01(i,j,h),tij(i,j,h),bij(i,j,h)]
def listaD3ijh(i,j,h):
    lista=[]
    lista+=[funcion(Vij(i,j,h)),funcion(wij11(i,j,h)),funcion(wij10(i,j,h))]
    lista+=[funcion(wij0menos1(i,j,h)),funcion(wijmenos1menos1(i,j,h))]
    lista+=[funcion(wijmenos10(i,j,h)),funcion(wij01(i,j,h))]
    lista+=[funcion(wijmenos1menos1(i+1,j+1,h)),funcion(tij(i,j,h))]
    
    lista+=[funcion(wijmenos10(i+1,j,h)),funcion(bij(i,j-1,h))]
    
    lista+=[funcion(wij01(i,j-1,h)),funcion(tij(i-1,j-1,h))]
    
    lista+=[funcion(wij11(i-1,j-1,h)), funcion(bij(i-1,j-1,h))]
    
    lista+=[funcion(wij10(i-1,j,h)),funcion(tij(i-1,j,h))]
    
    lista+=[funcion(wij0menos1(i,j+1,h)),funcion(bij(i,j,h))]
    
    lista+=[funcion(Vij(i+1,j+1,h)),funcion(wij0menos1(i+1,j+1,h))]
    
    lista+=[funcion(wij01(i+1,j,h)),funcion(Vij(i+1,j,h))]
    
    lista+=[funcion(wijmenos1menos1(i+1,j,h)),funcion(wij11(i,j-1,h))]
    
    lista+=[funcion(Vij(i,j-1,h)),funcion(wijmenos10(i,j-1,h))]
    
    lista+=[funcion(wij10(i-1,j-1,h)),funcion(Vij(i-1,j-1,h))]
    lista+=[funcion(wij01(i-1,j-1,h)),funcion(wij0menos1(i-1,j,h))]
    lista+=[funcion(Vij(i-1,j,h)),funcion(wij11(i-1,j,h))]
    lista+=[funcion(wijmenos1menos1(i,j+1,h)),funcion(Vij(i,j+1,h))]
    lista+=[funcion(wij10(i,j+1,h)),funcion(wijmenos10(i+1,j+1,h))]
    return lista


masku0=[[1],[27/28,27/56,-27/56,-27/28,-27/56,27/56],[27/28,-6191/4480,27/56,83/1120,-27/56,6523/4480,-27/28,6191/4480,-27/56,-83/1120,27/56,-6523/4480]]
masku0.append([-857/3360,3293/13440,-167/67200,-359/6720,257/16800,-2083/16800,271/1344,-15437/67200,-1633/13440,857/3360,-3293/13440,167/67200,359/6720,-257/16800,2083/16800,-271/1344,15437/67200,1633/13440])
masku1=[[1],RotateRight(masku0[1],1),RotateRight(masku0[2],2),RotateRight(masku0[3],3)]
masku2=[[1],RotateRight(masku1[1],1),RotateRight(masku1[2],2),RotateRight(masku1[3],3)]
masku3=[[1],RotateRight(masku2[1],1),RotateRight(masku2[2],2),RotateRight(masku2[3],3)]
masku4=[[1],RotateRight(masku3[1],1),RotateRight(masku3[2],2),RotateRight(masku3[3],3)]
masku5=[[1],RotateRight(masku4[1],1),RotateRight(masku4[2],2),RotateRight(masku4[3],3)]
masku0=Flatten(masku0)
masku1=Flatten(masku1)
masku2=Flatten(masku2)
masku3=Flatten(masku3)
masku4=Flatten(masku4)
masku5=Flatten(masku5)

maske0=[[10/21],[-27/28,-27/56,0,0,0,-27/56],[-27/28,75/28,-27/56,0,0,0,0,0,0,0,-27/56,75/28],[10/21,-27/56,-27/56,5/21,0,0,0,0,0,0,0,0,0,0,0,5/21,-27/56,-27/56]]
maske1=[[10/21],RotateRight(maske0[1],1),RotateRight(maske0[2],2),RotateRight(maske0[3],3)]
maske2=[[10/21],RotateRight(maske1[1],1),RotateRight(maske1[2],2),RotateRight(maske1[3],3)]
maske3=[[10/21],RotateRight(maske2[1],1),RotateRight(maske2[2],2),RotateRight(maske2[3],3)]
maske4=[[10/21],RotateRight(maske3[1],1),RotateRight(maske3[2],2),RotateRight(maske3[3],3)]
maske5=[[10/21],RotateRight(maske4[1],1),RotateRight(maske4[2],2),RotateRight(maske4[3],3)]
maske0=Flatten(maske0)
maske1=Flatten(maske1)
maske2=Flatten(maske2)
maske3=Flatten(maske3)
maske4=Flatten(maske4)
maske5=Flatten(maske5)

maskz0=[[31/42],[0,0,0,-27/56,-27/56,0],[0,613/448,0,-321/4480,0,653/4480,-27/56,587/448,-27/56,321/4480,0,-653/4480]]
maskz0.append([1803/11200,-5021/14000,-7683/28000,2021/33600,40829/336000,-70639/336000,523/4200,-35689/336000,28979/336000,2591/33600,-247/2000,-831/4000,1993/11200,-40829/336000,70639/336000,-523/4200,35689/336000,-28979/336000])
maskz1=[[31/42],RotateRight(maskz0[1],1),RotateRight(maskz0[2],2),RotateRight(maskz0[3],3)]
maskz2=[[31/42],RotateRight(maskz1[1],1),RotateRight(maskz1[2],2),RotateRight(maskz1[3],3)]
maskz3=[[31/42],RotateRight(maskz2[1],1),RotateRight(maskz2[2],2),RotateRight(maskz2[3],3)]
maskz4=[[31/42],RotateRight(maskz3[1],1),RotateRight(maskz3[2],2),RotateRight(maskz3[3],3)]
maskz5=[[31/42],RotateRight(maskz4[1],1),RotateRight(maskz4[2],2),RotateRight(maskz4[3],3)]

maskz0=Flatten(maskz0)
maskz1=Flatten(maskz1)
maskz2=Flatten(maskz2)
maskz3=Flatten(maskz3)
maskz4=Flatten(maskz4)
maskz5=Flatten(maskz5)
def VIJ(i,j,h):
    return funcion(Vij(i,j,h))
def Uij11(i,j,h):
    return Dot(masku0,listaD3ijh(i,j,h))
def Uij10(i,j,h):
    return Dot(masku1,listaD3ijh(i,j,h))
def Uij0menos1(i,j,h):
    return Dot(masku2,listaD3ijh(i,j,h))
def Uijmenos1menos1(i,j,h):
    return Dot(masku3,listaD3ijh(i,j,h))
def Uijmenos10(i,j,h):
    return Dot(masku4,listaD3ijh(i,j,h))
def Uij01(i,j,h):
    return Dot(masku5,listaD3ijh(i,j,h))
def BEij11(i,j,h):
    return Dot(maske0,listaD3ijh(i,j,h))
def BEij10(i,j,h):
    return Dot(maske1,listaD3ijh(i,j,h))
def BEij01(i,j,h):
    return Dot(maske5,listaD3ijh(i,j,h))
def Zij11(i,j,h):
    return Dot(maskz0,listaD3ijh(i,j,h))
def Zij10(i,j,h):
    return Dot(maskz1,listaD3ijh(i,j,h))
def Zij0menos1(i,j,h):
    return Dot(maskz2,listaD3ijh(i,j,h))
def Zijmenos1menos1(i,j,h):
    return Dot(maskz3,listaD3ijh(i,j,h))
def Zijmenos10(i,j,h):
    return Dot(maskz4,listaD3ijh(i,j,h))
def Zij01(i,j,h):
    return Dot(maskz5,listaD3ijh(i,j,h))
def interpolanteSuperficie(h):
    z1=np.linspace(0,1,20)
    z2=np.linspace(0,1,20)
    x=[]
    y=[]
    z=[]
    error=[]
    for i in z1:
        for j in z2:
            ii=floor((i+j)/(2*h))
            jj=floor((i-j)/(2*h))
            if((ii-jj)*h<=j<=(ii-jj+1)*h):
                BBcoefs=[VIJ(ii,jj,h),Uij11(ii,jj,h),Uij10(ii,jj,h),BEij11(ii,jj,h),Zij11(ii,jj,h),BEij10(ii,jj,h),Uijmenos1menos1(ii+1,jj+1,h)]
                BBcoefs+=[Zij0menos1(ii+1,jj+1,h),Zijmenos10(ii+1,jj,h),Uijmenos10(ii+1,jj,h),VIJ(ii+1,jj+1,h)]
                BBcoefs+=[Uij0menos1(ii+1,jj+1,h),BEij01(ii+1,jj,h),Uij01(ii+1,jj,h),VIJ(ii+1,jj,h)]
                tri=[Vij(ii,jj,h),Vij(ii+1,jj+1,h),Vij(ii+1,jj,h)]
            else:
                BBcoefs=[VIJ(ii,jj,h),Uij01(ii,jj,h),Uij11(ii,jj,h),BEij01(ii,jj,h),Zij01(ii,jj,h),BEij11(ii,jj,h)]
                BBcoefs+=[Uij0menos1(ii,jj+1,h),Zij10(ii,jj+1,h),Zijmenos1menos1(ii+1,jj+1,h),Uijmenos1menos1(ii+1,jj+1,h)]
                BBcoefs+=[VIJ(ii,jj+1,h),Uij10(ii,jj+1,h),BEij10(ii,jj+1,h),Uijmenos10(ii+1,jj+1,h),VIJ(ii+1,jj+1,h)]
                tri=[Vij(ii,jj,h),Vij(ii,jj+1,h),Vij(ii+1,jj+1,h)]
            A=np.array([ [tri[0][0],tri[1][0],tri[2][0] ],[ tri[0][1],tri[1][1],tri[2][1] ],[1,1,1] ])
            b=np.array([i,j,1])
            solucion=np.linalg.solve(A,b)
            #print(solucion)
            polinomio=[]
            for k in range(0,15):
                polinomio.append( (factorial(4)/(factorial(ind[k][0])*factorial(ind[k][1])*factorial(ind[k][2])))*solucion[0]**ind[k][0]*solucion[1]**ind[k][1]*solucion[2]**ind[k][2])
            val=Dot(polinomio,BBcoefs)
            x.append(i)
            y.append(j)
            z.append(val)
            error.append(abs(val-funcion([i,j])))
    ax = plt.axes(projection='3d')    
    #ax.plot3D(x, y, z)
    ax.plot_trisurf(x, y, error, cmap=cm.jet, linewidth=0.1)
   
interpolanteSuperficie(1/32)    
#print(listaDijh(0,0,0.1))    