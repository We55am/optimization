#!/usr/bin/env python
from random import *
import numpy as np
import sympy as sym


def halving_method(F, x, a, b, sigma):
    xm = (b-a)/2
    L = b-a
    x1 = a + L/4
    x2 = b - L/4
    
    Fm = F.subs(x, xm)
    F1 = F.subs(x, x1)
    F2 = F.subs(x, x2)

    while (L > sigma):
        if (F1 < Fm):
            b = xm
            xm = x1
        elif (F2 < Fm):
            a = xm
            xm = x2
        else:
            a = x1
            b = x2
            
        L = b-a
        x1 = a + L/4
        x2 = b - L/4
        Fm = F.subs(x, xm)
        F1 = F.subs(x, x1)
        F2 = F.subs(x, x2)

    return xm

def main():
    print ("Interval Halving Method For Unimodal Function")

    ## Objective Function
    print ("Objective Function")
    x = sym.symbols('x')
    F = (x**2) + (54/x)
    print(F)

    ## Desgin Parameters
    a = 0.1             # lower bound of the design variable
    b = 10              # upper bound of the design variable
    sigma = 0.00001     # Accuracy of the result

    ## Interval Halving Method
    xm = halving_method(F, x, a, b, sigma)
    print("Local minimum Value is: " + str(xm))

if __name__ == "__main__":
    main()
