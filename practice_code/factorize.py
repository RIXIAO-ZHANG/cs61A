def factorize(n, k=2):
    if n == k:
        return 1
    elif n < k:
        return 0
    elif n % k > 0:
        return factorize(n,k+1)
    return factorize(n, k+1) + factorize(n//k,k)

print(factorize(7))
print(factorize(12))
print(factorize(36))
