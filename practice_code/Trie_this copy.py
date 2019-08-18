def tree(label,branches=[]):
    #input verification
    for branch in branches:
        assert(is_tree(branch))
    return [label] + list(branches)


def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def add_word(trie, word):
    if word is Link.empty:
        return
    branch = None
    for b in branches(trie):
        if label(b) == word[0]:
            branch = b
    if not branch:
        branch = tree(word[0])
        branches(trie).append(branch)
    add_word(branch, word[1:])
