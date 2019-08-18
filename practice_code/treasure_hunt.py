def leap(pots):
    if len(pots) == 0:
        return 0
    return max(leap(pots[2:])+ pots[0], leap(pots[1:]))



print(leap([2,4,3]))
print(leap([4,20,9,3,6,2]))
