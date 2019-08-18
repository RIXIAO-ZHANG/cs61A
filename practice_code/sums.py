def sums(n,k):
    if k == 1:
        return [[n]]
    y = []
    for x in range(1,n):
        y.extend([[x] + s for s in sums(n-x, k-1)])
    return y


print(sums(2,2))
print(sums(2,3))
print(sums(4,2))
print(sums(5,3))
print(sums(5,1))
