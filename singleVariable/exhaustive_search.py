#!/usr/bin/env python
import numpy as np
import sympy as sym


def exhaustive_search(F, x, a, b, n):
    delta_x = (b-a)/n
    x1 = a
    x2 = x1 + delta_x
    x3 = x2 + delta_x

    while (x3 < b):
        f1 = F.subs(x, x1)
        f2 = F.subs(x, x2)
        f3 = F.subs(x, x3)
        if (f2 <= f1 and f2 <= f3):
            return x2
            break
        x1 = x2
        x2 = x3
        x3 = x3 + delta_x
        
    return False
    

def main():
    print "Single Variable -- Exhaustive Method"

    ## Objective Function
    print "Objective Function: "
    x = sym.symbols('x')
    F = (x**2) + (54/x)
    print F
    
    ## Desgin Parameters
    a = 0.5     # upper bound of the design variable
    b = 5       # lower bound of the design variable
    n = 100     # number of intermediate points

    ## Exhaustive Search Method
    val = exhaustive_search(F, x, a, b, n)
    if(val):
        print("The minimum is: " + str(val))
    else:
        print "couldn't find local minimum, consider changing the boundaires"

        
if __name__ == "__main__":
    main()
