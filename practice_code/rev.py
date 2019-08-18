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



def rev(s):
    """Yield the elements in Link instance s in reverse order.
    >>> list(rev(Link(1, Link(2, Link(3)))))
    [3, 2, 1]
    >>> next(rev(Link(2, Link(3))))
    3
     """
    if s is not Link.empty:
        yield from rev(s.rest)
        yield s.first

"""
yield from interables = for item in iterables:
                            yield item
"""
