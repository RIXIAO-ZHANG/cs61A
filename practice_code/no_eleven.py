def no_eleven(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6],[1]]
    else:
        a,b = no_eleven(n-1) , no_eleven(n-2)
        return [ [6] + s for s in a] +  [ [1,6] + s for s in b]


print(no_eleven(4))

"""
    Error : [ s.insert(0,6) for s in a] +  [ [1,6] + s for s in b]
    
    [print(x) for x in [1,2,3]]
    [None, NO]


"""
