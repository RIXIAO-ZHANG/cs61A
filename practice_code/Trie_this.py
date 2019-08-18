class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches

def make_trie(words):
    """ Makes a tree where every node is a letter of a word.
        All words end as a leaf of the tree.
        words is given as a list of strings.
    """
    trie = Tree('')
    for word in words:
        add_word(trie, word)
    return trie

def add_word(trie, word):
    if word == '':
        return

    branch = None
    for b in trie.branches:
        if b.label == word[0]:
            branch = b
    if not branch:
        branch = Tree(word[0])
        trie.branches.append(branch)
    add_word(branch, word[1:])

def get_words(trie):
    """
    >>> get_words(make_trie(['this', 'is', 'the', 'trie']))
    ['this', 'the', 'trie', 'is']
    """
    if trie.is_leaf():
        return [trie.label]
return sum([[trie.label + word for word in get_words(branch)] for branch in trie.branches], [])
