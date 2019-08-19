"""
An (n)-repeater for a single-argument function f takes a single argument x,
calls f(x) n times, then returns an (n + 1)-repeater for f.

"""
def repeater(f,n):
    def g(x):
            repeat(f,x,n)
        return repeater(f,n+1)
    return g



def repeat(f,x,n):
    if n > 0:
        f(x)
        repeat(f,x,n-1)
