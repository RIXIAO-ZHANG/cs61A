
def count_groupings1(n):
    if n == 1:
        return 1
    total = 0
    i = 1
    while i < n:
        total += count_groupings1(i) * count_groupings1(n-i)
        i += 1
    return total
