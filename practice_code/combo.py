def combo(a,b):
    if a == 0 or b == 0:
        return a+b
    elif a % 10 == b % 10:
        return combo(a//10,b//10) * 10 +  a % 10
    return min(combo(a//10,b)*10 + a%10 ,combo(b//10,a)*10 + b%10)

print(combo(531,432))
print(combo(531,4321))
print(combo(1234,9123))
print(combo(0,321))
