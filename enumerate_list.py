def enumerate_list(lst):
    index = -1
    new = []
    for element in lst:
        if element != "":
            index += 1
            new.append(f"{index}. {element}")
    return new

def enumerate_backwards(lst):

    index = -1
    new = []
    for element in lst:
        if element != "":
            index += 1
            new.append(f"{index}. {element[::-1]}")
    return new
