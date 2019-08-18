def counter(base):
    def parse(digit,lst):
        if digit == 'done':
            return sum(lst)
        elif digit >= base:
            return lambda x: parse(x,lst)
        else:
            return lambda x: parse(x,[elem*base for elem in lst] + [digit])
    return lambda x : parse(x,[])

binary = counter(2)
print(binary('done'))
print(binary(1)(0)(1)(1)('done'))
print(binary(1)(2)(3)(0)(1)('done'))

quaternary = counter(4)
print(quaternary(1)(2)(3)(0)(1)('done'))
