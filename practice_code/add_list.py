def add_list(list1,list2):
    return [ list1[i] + list2[i] for i in range(len(list1))]

def hamming_distance(list1,list2):
    return sum([ elem % 2 for elem in add_list(list1,list2)])

def hamming_neareast_neighbor(data, test_point):
    return min(data, key=lambda x: hamming_distance(x,test_point))
