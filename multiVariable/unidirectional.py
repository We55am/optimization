#!/usr/bin/env python
import sympy as sym
import numpy as np
import sys
sys.path.append('../singleVariable/')
import bounding_phase_method
import interval_halving_method
from random import *

def subs(F, x, x_v):
    for i in range(len(x)):
        F = F.subs(x[i], x_v[i])
    return F


def unidirectional_search(F, x, x_t, s_t):
    x_v = []
    alpha = sym.symbols('alpha')
    for i in range(len(x)):
        x_v = x_v + [x_t[i] + alpha*s_t[i]]
    new_F = subs(F, x, x_v)
    [a, b] = bounding_phase_method.bounding_method(new_F, alpha, 0, 0.001, 10000)
    min_alpha = interval_halving_method.halving_method(new_F, alpha, a, b, 0.000001)
    result = []
    for i in range(len(x)):
        result += [x_v[i].subs(alpha, min_alpha)]
        
    return result

def main():
    print("Unidirectional Search for Multivaraible Optimization Problem")

    ## Objective Function
    
    x = [sym.symbols('x1'), sym.symbols('x2')]
    F = (x[0] - 10)**2 + (x[1] - 10)**2
    print(F)

    ## Design Parameters
    x_t = [2, 2]
    s_t = [15, 12]
    
    ## Unidirectional Search Method
    xm = unidirectional_search(F, x, x_t, s_t)

    print("Local minimum value is: " + str(xm))
    

if __name__ == "__main__":
    main()
