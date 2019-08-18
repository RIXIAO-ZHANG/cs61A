def tree(label,branches=[]):
    #input verification
    for branch in branches:
        assert(is_tree(branch))
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def pile(t):
    p = {}
    def gether(u, path_so_far):
        if is_leaf(u):
            p[label(u)] = path_so_far
        for b in branches(u):
            gether(b, (label(u), path_so_far))
    gether(t, ())
    return p
