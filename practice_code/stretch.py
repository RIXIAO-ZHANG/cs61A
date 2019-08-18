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


def stretch(s,repeat=0):
    """Replicate the kth element k times, for all k in s.
    >>> a = Link(3, Link(4, Link(5, Link(6))))
    >>> stretch(a)
    >>> print(a)
    <3, 4, 4, 5, 5, 5, 6, 6, 6, 6>
    """
    if s is not Link.empty:
        for i in range(repate):
            s.rest = Link(s.first, s.rest)
            s = s.rest
        stretch(s.rest,repeat+1)
