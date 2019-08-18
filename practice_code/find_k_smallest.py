def find_k_smallest(lst,k,func):
    if  k <= 0 or len(lst) == 0:
        return []
    current_min = min(lst, key=func)

    return
