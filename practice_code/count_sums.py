def count_sums(n,f,m):
    if n == 0:
        return 1
    elif n < 0 or m <= 0 :
        return 0
    return count_sums(n-m,f,f(m)) + count_sums(n,f,f(m))


print(count_sums(6,lambda k: k - 1, 4))   # 2: 4 + 2    3+2+1
print(count_sums(12,lambda k: k - 2, 12))  #4: 12 , 10 + 2, 8 + 4, 6 + 4 + 2
print(count_sums(11,lambda k: k // 2, 8))  #1: 8 + 2 + 1
