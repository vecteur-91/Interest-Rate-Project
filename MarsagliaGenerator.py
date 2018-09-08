# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:11:00 2018

@author: SIVA
"""

### Load Packages
import numpy as np
from matplotlib import*
import matplotlib.pyplot as plt

def marsaglia(n,seed=778):
    np.random.seed(seed)
    u1=np.random.normal(0,1,n)
    u2=np.random.normal(0,1,n)
    v1=2*u1-1
    v2=2*u2-1

    normal=[]
    i=0
    while (i < n):
        if((v1[i]**2+v2[i]**2) < 1):
            w=v1[i]**2+v2[i]**2
            z1=v1[i]*np.sqrt(-2*np.log(w)/w)
            z2=v2[i]*np.sqrt(-2*np.log(w)/w)
            normal.append([z1,z2])
        i+=1
    return normal


normal_values = marsaglia(100000)

normal_values = np.array(normal_values)
x = normal_values[:,0]
y = normal_values[:,1]

plt.scatter(x,y,s=1)
