#!/usr/bin/env python
import sympy as sym
import numpy as np
import sys
sys.path.append('../')
import himmelblau_function as fun
import unidirectional

def mag(delta):
    result = 0
    for i in range(len(delta)):
        result += delta[i]**2
    return np.sqrt(result)

def subs(F, x, x_v):
    for i in range(len(x)):
        F = F.subs(x[i], x_v[i])
    return F

def box_evolutionary(F, x, x_0, delta, sigma):
    x_current = x_0
    F_current = subs(F, x, x_current)
    resize_flag = True
    
    while(mag(delta) > sigma):
        x1 = [(x_current[0] - (delta[0]/2)), (x_current[1]) - (delta[1]/2)]
        x2 = [(x_current[0] - (delta[0]/2)), (x_current[1]) + (delta[1]/2)]
        x3 = [(x_current[0] + (delta[0]/2)), (x_current[1]) - (delta[1]/2)]
        x4 = [(x_current[0] + (delta[0]/2)), (x_current[1]) + (delta[1]/2)]
        
        if F_current > subs(F, x, x1):
            x_current = x1
            resize_flag = False
        if F_current > subs(F, x, x2):
            x_current = x2
            resize_flag = False
        if F_current > subs(F, x, x3):
            x_current = x3
            resize_flag = False
        if F_current > subs(F, x, x4):
            x_current = x4
            resize_flag = False

        F_current = subs(F, x, x_current)
        
        if resize_flag == True:
            delta[0] = delta[0]/2
            delta[1] = delta[1]/2

        resize_flag = True
        
        
    return x_current

def main():
    print "Box's Evolutionary Search for Multivaraible Optimization Problem"

    ## Objective Function
    [F, x] = fun.himmelblau()
    print F

    ## Design Parameters
    x_0 = unidirectional.unidirectional_search(F, x, [1.0, 1.0], [9.0, 9.0]) # nearest best solution (can be any random solution also)
    delta = [1.5, 1.5] # size reduction parameter
    sigma = 0.000001     # Termination
    
    ## Box's Evolutionary Search Method
    xm = box_evolutionary(F, x, x_0, delta, sigma)

    print("Local minimum value is: " + str(xm))
    



if __name__ == "__main__":
    main()
