import sympy as sym
import numpy as np
from random import *


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
    print("The Boundaries are [" + str(array[0]) + ", " + str(array[2]) + "]")


if __name__ == "__main__":
    main()
