def replace_with_sum(t):
    if is_leaf(t):
        return tree(lable(t))
    new_branches = [ replace_with_sum(branch) for branch in branches(t)]
    branch_sum = sum ([label(branch) for branch in new_branches])
    return tree(branch_sum+label(t), new_branches)
