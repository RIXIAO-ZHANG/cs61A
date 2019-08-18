def is_sorted(n):
    if n < 10:
        return True
    elif n % 10 <= (n//10)%10:
        return is_sorted(n//10)
    else:
        return False

print(is_sorted(987654321))
print(is_sorted(9087654321))
print(is_sorted(4))
print(is_sorted(555555555555))
