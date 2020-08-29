#!/usr/bin/env python
import sympy as sym
import numpy as np
import sys
sys.path.append('../')
import himmelblau_function as fun
import unidirectional

def subs(F, x, x_v):
    for i in range(len(x)):
        F = F.subs(x[i], x_v[i])
    return F

def create_simplex(x_base, scale_factor):
    n = len(x_base)
    if n == 3:
        d = 0.25
    else:
        d = (np.sqrt(n+1) - 2)/(n - 3)
        
    simplex = [[0.0 for x in range(n)] for y in range(n+1)]
    simplex[0] = x_base

    for i in range(n):
        for j in range(n):
            if i == j:
                simplex[i+1][j] = simplex[i][j] + scale_factor
            else:
                simplex[i+1][j] = simplex[i][j] + (d*scale_factor)
                
    return simplex


def simplex(F, x, x_base, gamma, beta, sigma, scale_factor):
    n = len(x)
    simplex = create_simplex(x_base, scale_factor)

    xh = simplex[0]
    xh_indx = 0
    xg = simplex[0]
    xl = simplex[0]

    while(1):

        for i in range(n+1):
            value = subs(F, x, simplex[i])
            if value > subs(F, x, xh):
                xh = simplex[i]
                xh_indx = i
            elif value < subs(F, x, xl):
                xl = simplex[i]
        for i in range(n+1):
            value = subs(F, x, simplex[i])
            if value > subs(F, x, xg) and value < subs(F, x, xh):
                xg = simplex[i]

        t_sum = [0.0, 0.0]
        for i in range(n+1):
            if simplex[i] is not xh:
                for j in range(n):
                    t_sum[j] += simplex[i][j]

        xc = [0.0, 0.0]
        xr = [0.0, 0.0]
        for i in range(n):
            xc[i] = t_sum[i]/n
            xr[i] = (2*xc[i]) - xh[i]

        F_xr = subs(F, x, xr)
        F_xh = subs(F, x, xh)
        F_xl = subs(F, x, xl)
        F_xg = subs(F, x, xg)
        F_xc = subs(F, x, xc)

        x_new = xr
        if F_xr < F_xl:
            for i in range(n):
                x_new[i] = ((1+gamma)*xc[i]) - (gamma*xh[i])
        elif F_xr >= F_xh:
            for i in range(n):
                x_new[i] = ((1-beta)*xc[i]) + (beta*xh[i])
        elif F_xg < F_xr and F_xr < F_xh:
            for i in range(n):
                x_new[i] = ((1-beta)*xc[i]) + (beta*xh[i])

        t_sum = 0.0
        for i in range(n+1):
            t_sum = ((subs(F,x,simplex[i]) - F_xc)**2)/(n+1)
        t_sum = float(t_sum)

        print(np.sqrt(t_sum))
        
        if np.sqrt(t_sum) <= sigma:
            break
        else:
            simplex[xh_indx] = x_new

    return xl

def main():
    print("Simplex Search Method for Multivaraible Optimization Problem")

    ## Objective Function
    [F, x] = fun.himmelblau()
    print(F)

    ## Design Parameters
    x_base = unidirectional.unidirectional_search(F, x, [1.0, 1.0], [9.0, 9.0]) # nearest best solution (can be any random solution also)
    #x_base = [0.0, 0.0]
    gamma = 2.0 # size reduction parameter
    sigma = 1     # Termination
    beta = 0.5
    scale_factor = 0.6
    
    ## Box's Evolutionary Search Method
    xm = simplex(F, x, x_base, gamma, beta, sigma, scale_factor)

    print("Local minimum value is: " + str(xm))


if __name__ == "__main__":
    main()
