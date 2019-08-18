def a_path(t,x):
    """Return a path from the root of t that ends with x.

    """
    if label(t) == x:
        return [x]

    for branch in branches(t):
        rest_of_path = a_path(b,x)
        if rest_of_path:
            return [label(t)] + rest_of_path
