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


def pascal_row(s):
    if s is Link.empty:
        return Link(1)
    start = Link(1)
    last, current = start, s

    while current.rest is not Link.empty:
        last.rest = Link(current.first + current.rest.first)
        last, current = last.rest, current.rest
    last.rest = Link(1)
    return start

def make_pascal_triangle(k):
    if k = 0:
        return Link.empty
    row = Link(1)
    end = Link(row)
    result = end

    while _ in range(k-1):
        row = pascal_row(row)
        end.rest = Link(row)
        end = end.rest
    return result
