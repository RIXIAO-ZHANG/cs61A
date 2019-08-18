def in_nested(v,L):
    if type(L) != list:
        return L == v
    else:
        return any([in_nested(v,elem) for elem in L])
L = [[[1], [6, 4, [5, [9]]], 7], 7, 7]
print(in_nested(9, L))
