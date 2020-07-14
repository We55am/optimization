#!/usr/bin/env python
import sympy as sym
import numpy as np
from random import *

def bounding_method(F, x, x_inital, delta, time_out):
    k = 0
    array = np.zeros(3)
    array[2] = x_inital

    fx = F.subs(x, x_inital)
    fx_neg = F.subs(x, (x_inital-delta))
    fx_pos = F.subs(x, (x_inital+delta))

    for i in range(time_out):
        if (fx_neg >= fx and fx >= fx_pos):
            break
        elif (fx_neg <= fx and fx <= fx_pos):
            delta *= -1
            break
        else:
            x_inital = random()*10
    
    for i in range(time_out):
        array[0] = array[1]
        array[1] = array[2]
        array[2] = array[2] + (2**i)*delta
        fxk1 = F.subs(x, array[2])
        fxk = F.subs(x, array[1])
        if (fxk1 >= fxk):
            break
    return [array[0], array[2]]


def main():

    print "Bounding Phase Method for Unimodal Functions"

    ## Objective Function
    x = sym.symbols('x')
    F = (x**2) + (54/x)
    print F

    ## Desgin Parameters
    x_inital = random()*10
    delta = 0.001
    time_out = 200

    ## Bounding
    [a, b] = bounding_method(F, x, x_inital, delta, time_out)
    print("The Boundaries are [" + str(b) + ", " + str(a) + "]")

    
if __name__ == "__main__":
    main()
