
from math import pi


def identity(k):
    return k

def cube(k):
    return pow(k,3)

def sum_pii(k):
    return 8 / ((4*k-3)*(4*k-1))




"hiher order function"
def summation(n,term):
    sum = 0
    i = 1

    while i <= n:
        sum += term(i)
        i += 1
    return sum


"lower order function"
def sum_naturals(n):

    return summation(n,identity)

def sum_cube(n):

    return summation(n,cube)

def sum_pi(n):

    return summation(n,sum_pii)
