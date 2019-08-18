def kbonacci(n,k):
    if n < k-1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = 1
        while i < n:
            total += kbonacci(n-i,k)
            i += 1
        return total

print(kbonacci(3,4))
print(kbonacci(9,4))
print(kbonacci(4,2))
print(kbonacci(8,2))
