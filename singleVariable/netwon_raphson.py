#!/usr/bin/env python
import sympy as sym
import numpy as np
from random import *


def netwon_rapshon(F, x, delta_x, inital_guess, error):
    x1 = inital_guess
    F_x1 = F.subs(x, x1)
    ## central difference method
    # First Derivative
    F_dot_x1 = (F.subs(x, x1+delta_x) - F.subs(x, x1-delta_x))/(2*delta_x)
    # second Derivative
    F_dot_dot_x1 = (F.subs(x, x1+delta_x) - 2*F_x1 + F.subs(x, x1-delta_x))/(delta_x)**2
    x_new = x1 - (F_dot_x1/F_dot_dot_x1)

    F_dot_x_new = (F.subs(x, x_new+delta_x) - F.subs(x, x_new-delta_x))/(2*delta_x)
    while(abs(F_dot_x_new) > error):
        F_x_new = F.subs(x, x_new)
        F_dot_dot_x_new = (F.subs(x, x_new+delta_x) - 2*F_x_new + F.subs(x, x_new-delta_x))/(delta_x)**2
        x_new  = x_new - (F_dot_x_new/F_dot_dot_x_new)
        F_dot_x_new = (F.subs(x, x_new+delta_x) - F.subs(x, x_new-delta_x))/(2*delta_x)

    return x_new
    
def main():
    print "Netwon-Raphson Method"

    ## Objective Function
    
    x = sym.symbols('x')
    F = (x**2) + (54/x)
    print F

    ## Design Parameters
    delta_x = 0.001
    inital_guess = 1
    error = 0.0001

    
    ## Netwon-Rapshon
    xm = netwon_rapshon(F, x, delta_x, inital_guess, error)

    print("Local minimum value is: " + str(xm))


if __name__ == "__main__":
    main()
