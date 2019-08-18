def is_subseq(w1,w2):
    """
     Returns True if w1 is a subsequence of w2 and False otherwise.
          >>> is_subseq("word", "word")
          True
          >>> is_subseq("compute", "computer")
          True
          >>> is_subseq("put", "computer")
          True
          >>> is_subseq("computer", "put")
          False
          >>> is_subseq("sin", "science")
          True
          >>> is_subseq("nice", "science")
          False
          >>> is_subseq("boot", "bottle")
          False
          >>> is_subseq("a", "bottle")
          False
    """
    if not w1:
        return True
    elif not w2:
        return False

    with_elem = w1[0] == w2[0] and is_subseq(w1[1:],w2[1:])
    without_elem = is_subseq(w1,w2[1:])
    return with_elem or without_elem
