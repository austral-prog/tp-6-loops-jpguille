def power(base, exp):

    if exp >= 0:
        return (base ** exp)

def sum_of_powers(base, max_exp):
    suma = 0
    for exp in range(0, max_exp+1):
        suma += power(base, exp)
    return suma
