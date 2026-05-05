def put(value, lst):

    for i in range(len(lst)):
        if "" == lst[i]:
            lst[i] = value
            return i
    return -1

def remove(value, lst):
    contador = 0
    for i in range(len(lst)):
        if lst[i] == value:
            lst[i] = ""
            contador += 1
    return contador
