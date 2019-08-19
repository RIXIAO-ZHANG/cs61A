"""
Definition:
A combo of a non-negative integer n is the result of
adding or multiplying the digits of n from left to right, starting with 0.
For n = 357, combos include 15 = (((0+3)+5)+7),
35 = (((0∗3)+5)∗7), and 0 = (((0∗3)∗5)∗7), as well as 0, 7, 12, 22, 56, and 105.
But 36=((0+3)∗(5+7))is not a combo of 357.
"""


def is_combo(n,k):
    if  k == 0
        return True
    if  n == 0
        return False

    rest, last = n // 10, n % 10
    added = k >= last and is_combo(rest, k-last)
    multiplied = k % last == 0 and is_combo(rest, k//last)
    return added or multiplied
