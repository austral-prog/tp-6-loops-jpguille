def index_of(target, lst):

    for i in range(len(lst)):
        if target == lst[i]:
            index = len(lst[:i])
            return index
    return -1

def index_of_by_index(target, lst, start):

    for i in range(start, len(lst)):
        if target == lst[i]:
            index = len(lst[:i])
            return index
    return -1

def index_of_empty(lst):

    for i in range(len(lst)):
        if "" == lst[i]:
            index = len(lst[:i])
            return index
    return -1


