def plus(n):
    if n:
        return max(plus(n//10)+n%10, plus(n//100)+n%100)
    return 0



def plusses(n,cap):
    if n < 10 and n < cap:
        return 1
    elif n < 10 and n >= cap:
        return 0
    else:
        return plusses(n//10,cap-(n%10)) + plusses(n//100,cap-(n%100))



print(plus(123456)) #12+34+56 = 102
print(plus(1604)) # 1+60+4 = 65
print(plus(160450)) # 1+60+4+50 = 115

print(plusses(123,16))
print(plusses(2018,38))
print(plusses(1,2))
