def trail_of_treats(G):
    return trail_helper(G,0,0)


def trail_helper(G,x,y):
    left_bound, right_bound = 0, len(G[0])
    uppper_bound, bottom_bound = len(G[0]), 0

    if x == n and y == n:
        return G[x][y]

    if x < left_bound or x > right_bound:
        return -1

    treats_at_the_place = G[x][y]
    up = trail_helper(G,x, y+1)
    down = trail_helper(G,x, y-1)
    left = trail_helper(G, x-1, y)
    right = trail_helper(G, x+1, y)
    return treats_at_the_place + max(up,down,left,right)
