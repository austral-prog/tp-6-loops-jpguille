def countdown(n):
    new = []
    while n >= 0:
        new.append(n)
        n = n - 1
    return new


def double_until(limit):

    i = 1
    lst = [i]
    if limit < 1:
        return []
    while i*2 <= limit:
         i *= 2
         lst.append(i)
    return lst
