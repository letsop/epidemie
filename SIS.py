#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:56:44 2021

@author: postel
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def f2(X, t):
    """
    :param X: vecteur (S, I) (2 lignes)
    :param t: temps de condition initiale (réel)
    :return: vecteur second membre de l'équation
    """
    Y = np.asarray([-r * X[1] * X[0] + a * X[1], r * X[1] * X[0] - a * X[1]])
    return Y


a=1/7
r=0.1
T=100
N=1000
X0=np.array([0.3,0.7])
t=np.linspace(0,T,N)
X=odeint(f2,X0,t)
plt.plot(t,X[:,0],label='s')
plt.plot(t,X[:,1],label='I')
plt.legend()