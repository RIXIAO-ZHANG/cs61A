def link_iterator(link):
    if link is not Link.empty:
        yield link.first
        yield from link_iterator(link.rest)


def link_iterator(link):
    while link is not Link.empty:
        yield link.first
        link = link.rest
