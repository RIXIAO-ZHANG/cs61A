class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

def split(s, pred):
    satisfy, not_satisfy = Link.empty, Link.empty
    while s is not Link.empty:
        rest = s.rest
        if pred(s.first):
            satisfy, s.rest = s, satisfy   # like Link(first,rest)
        else:
            not_satisfy, s.rest = s, not_satisfy
        s = rest
    return satisfy, not_satisfy
