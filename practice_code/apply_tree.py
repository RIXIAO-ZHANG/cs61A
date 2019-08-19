class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches

"""
Implement apply_tree, which takes in two trees.
The labels of the first tree are all functions.
Apply_tree should mutate the the second tree such that
each label is the result of applying each function in the first tree
to the corresponding node in the second tree.
"""
def apply_tree(fn_tree, val_tree):
    val_tree.label = fn_tree.label(val_tree.label)
    for i in range(len(fn_tree.branches)):
        apply_tree(fn_tree.branches[i], val_tree.branches[i])


"""
Definition:
A combo of a non-negative integer n is the result of
adding or multiplying the digits of n from left to right, starting with 0.
For n = 357, combos include 15 = (((0+3)+5)+7),
35 = (((0∗3)+5)∗7), and 0 = (((0∗3)∗5)∗7), as well as 0, 7, 12, 22, 56, and 105.
But 36=((0+3)∗(5+7))is not a combo of 357.
"""
def is_combo(n,k):
    if  k == 0:
        return True
    if  n == 0:
        return False

    rest, last = n // 10, n % 10
    added = k >= last and is_combo(rest, k-last)
    multiplied = k % last == 0 and is_combo(rest, k//last)
    return added or multiplied


"""
Implement make_checker_tree which takes in a tree, t containing digits
as its labels and returns a tree with functions
as labels (a function tree). When applied to another tree,
the function tree should mutate it so each label is True
if the label is a combo of the number formed by
concatenating the labels from the root to the corresponding node of t.
You may use is_combo in your solution.
"""
def make_checker_tree(t, so_far=0):
    new_path = so_far * 10 + t.label
    branches = [make_checker_tree(b, new_path) for b in t.branches]
    fn = lambda value: is_combo(new_path, value)
    return Tree(fn,branches)
