def count_N_children(t,n):
    if t.is_leaf():
        return 0

def pruning(t):
    def delete(t, d):
        if d % 2 == 0:
            t.branches = [b for b in t.branches if b.label >= t.label]
        else:
            t.branches = [b for b in t.branches if b.label <= t.label]
        for b in t.branches:
            delete(b,d+1)
    delete(t,0)
