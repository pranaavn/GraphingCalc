from math import *
from sympy import *
from sympy.abc import x
import numpy as np
def diff(f, value):
    fn = lambdify(x, f)
    h = 0.00000000001
    numerator = fn(value + h) - fn(value)
    slope = numerator / h
    return float("%.5f" % slope)

def diff2(yVal1, yVal2):
    h = 0.01
    numerator = yVal2 - yVal1
    slope = numerator / h
    return float("%.5f" % slope)

def trapz(yVal1, yVal2):
    rv = 0.5*(yVal1+yVal2)*0.00001
    return rv


'''def diff2(f, value):
    fn = lambdify(x, f)
    h = 0.00000000001
    numerator = fn(value + h) - 2*fn(value)+fn(value-h)
    slope = numerator / (h**2)
    return float("%.5f" % slope)'''

'''print("Function:")
f = input()
print("Value:")
val = float(input())
print (diff(f, val))'''
