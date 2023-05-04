# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b4RhQgdtFUD7-ocl25Hodk9L8bM8IsA_
"""

from math import *
import numpy as np
import matplotlib . pyplot as plt
def funcion1(x):
    return np.exp(x) + 2**(-x)+ 2*cos(x)-6
def d1(x):
    return np.exp(x) - (np.log(2)/( 2**(x))) -2*sin(x)

l1=[]
l2=[]
# Ingreso datos de entrada para los diferentes métodos a trabajar
a = 1
b = 2

# guarda valores para newton
pi=1.5
#valorespara metodo secante
p0=1
p1=1.5

#guarda valores iniciales del error y del número de iteraciones
tol = 0.000000001  #float(input("Ingrese el valor de la tolerancia: "))
nmax = 20 #float(input("Ingrese el número máximo de iteraciones: "))
error = 100
e=100
niter = 0
# Método de  Newton

#Evaluacion de la función en los puntos a, b y m

i=1
print("# iter  \t\t P  \t\t error")
print("{0} \t\t {1:6.4f}  \t {2:6.4f}".format(i, pi, error ))

# ciclo iterativo newton
while error > tol and i <= nmax:
   
    fa=funcion1(pi)  
    da=d1(pi)
    p = pi - (fa/da)
    error = abs(p - pi)

    pi=p
    
    i += 1
    l2.append(error)
    print("{0} \t\t {1:15.15f} \t {2:15.15f}".format(i, p,error ))
    

print("La raíz de la función dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:15.15f}".format(a,b,p))

# ciclo iterativo secante
while e > tol and i <= nmax:
   
    fa=funcion1(p0)  
    fb=funcion1(p1)
    p = p1 - (fb*(p1-p0))/(fb-fa)
    
    e = abs(p1 - p0)
    p0=p1
    p1=p
    
    i += 1
    l1.append(e)





plt.plot(l2)
plt.plot(l1)
plt.xlabel("iteraciones")
plt.ylabel("error")
plt.show()