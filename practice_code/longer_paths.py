class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches

def longer_paths(t,n):
    def helper(t,n,can_start_path):
        paths = []
        if n <= 0:
            paths.append([t.label])
        for b in t.branches:
            for subpath in helper(b,n-1,False):
                paths.append([t.label] + subpath)
            if can_start_path:
                paths.extend(helper(b,n,True))
        return paths
    return helper(t,n,True)
