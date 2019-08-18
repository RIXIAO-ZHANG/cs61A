class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

def link_to_dict(L):
    """
    >>> L = Link(1, Link(2, Link(3, Link(4, Link(1, Link(5))))))
    >>> print(L)
    <1, 2, 3, 4, 1, 5>
    >>> link_to_dict(L)
    {1: [2, 5], 3: [4]}
    >>> print(L)
    <1, 3, 1>
    """
    D ={}
    while L is not Link.empty:
        key, value =  L.first, L.rest.first
        if key not in D:
            D[key] = [value]
        else:
            D[key].append(value)
        L.rest,L = L.rest.rest, L.rest.rest
        # L.rest = L.rest.rest remove all the values
    return D
