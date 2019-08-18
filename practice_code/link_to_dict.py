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
    d = {}
    while L is not Link.empty:
        key, value = L.first, L.rest.first
        if key is in d:
            d[key].append(value)
        else:
            d[key] = [value]
        L.rest, L = L.rest.rest, L.rest.rest
    return d
