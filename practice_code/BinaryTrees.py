def largest(t,x):
    if t is BTree.empty:
        return 0
    elif t.label >= x:
        return largest(t.left,x)
    y = largest(t.right,x)
    if y:
        return y
    return t.label

def second_largest(t,x):
    return largest(t,largest(t,x))
