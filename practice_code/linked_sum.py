class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest


def linked_sum(lnk, total):
    if total == 0:
        return 1
    if total < 0 or lnk is Link.empty:
        return 0
    else:
        with_first = linked_sum(lnk,total-lnk.first)
        without_first = linked_sum(lnk.rest,total)
        return with_first + without_first
