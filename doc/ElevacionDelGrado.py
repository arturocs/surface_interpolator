#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:41:38 2020

@author: abel
"""
def transponer(m):
    tras = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
    return tras

def ElevacionGrado(puntos):
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
        nuevaMatriz.append(ElevacionGrado(matriz[i]))
    return nuevaMatriz

def ElevacionGradoV(matriz):
    return ElevacionGradoU(transponer(matriz))
