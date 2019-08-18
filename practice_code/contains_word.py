def contains_words(str, word):
    if len(word) == 0:
        return True

    elif len(str) == 0:
        return False

    withWord =  str[0] == word[0] and contains_words(str[1:], word[1:])
    without = contains_words(str[1:], word)
    return withWord or without
