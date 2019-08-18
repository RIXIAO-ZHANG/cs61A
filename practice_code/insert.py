class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

def link_insert(lnklst,value,before):
    if lnklst is Link.empty:
        return Link.empty
    elif lnklst.first == before:
        return Link(value,lnklst)
    else:
        return Link(lnklst.first,link_insert(lnklst.rest,value,before))
