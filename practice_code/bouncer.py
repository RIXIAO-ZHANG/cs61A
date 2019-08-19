"""
Implement a function bouncer that takes in a linked list and an index k
and moves the value at index k of the link to the end.
You should mutate the input link.
"""


class Link:
    empty = ()
    def __init__(self, first, rest):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

def bouncer(link, k):
    if k == 0:
        swapper(link)
    else
        bouncer(link.rest, k-1)

def swapper(link):
    if link.rest is Link.empty
        return
    link.first, link.rest.first = link.rest.first, link.first
    swapper(link.rest)
