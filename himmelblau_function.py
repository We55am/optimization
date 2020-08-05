#!/usr/bin/env python
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def himmelblau():
    x = [sym.symbols('x1'), sym.symbols('x2')]
    F = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    return [F, x]

def main():
    print "Himmelblau Function ..."
    [F, x] = himmelblau()
    print F
    print "---------------------------------------------------------"
    print "It has one local maximum at x1 = -0.270845, x2 =-0.923039"
    print "Where f(x1, x2) = 181.617"
    print "and four identical local minima: "
    print "F(3.0,2.0) = 0.0"
    print "F(-2.805118,3.131312) = 0.0 "
    print "F(-3.779310,-3.283186) = 0.0 "
    print "F(3.584428,-1.848126) = 0.0 "
    fig = plt.figure(figsize=(6,5))
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes([left, bottom, width, height])
    start, stop, n_values = -3, 3, 100
    x_vals = np.linspace(start, stop, n_values)
    y_vals = np.linspace(start, stop, n_values)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2
    cp = plt.contour(X, Y, Z)
    #plt.colorbar(cp)
    ax.set_title('Contour Plot of Himmelblau Function')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    plt.show()
    

if __name__ == "__main__":
    main()
