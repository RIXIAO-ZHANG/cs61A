def combine(left,right):
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    if n < 10:
        return n
    else:
        return combine(n%10,reserve(n//10))

def remove(n,digit):
    removed = 0
    while n != 0:
        n, last = n // 10, n % 10
        if last == digit:
            removed = remove(n,digit)
    return reverse(removed)



print(remove(243132,3))
