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

def both(a,b):
    if a is Link.empty or b is Link.empty:
        return False
    if a.first > b.first
        a, b = b, a
    return a.first == b.first or both(a.rest, b)
