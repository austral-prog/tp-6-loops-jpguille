def sum_to_n(n):
    contador = 0
    if n <= 0:
        return 0
    else:
        for k in range(1, n + 1):
            contador += k
        return contador

def sum_evens(n):
    contador = 0
    if n <= 0:
        return 0
    else:
        for k in range(1, n + 1):
            if k % 2 == 0:
                contador += k
    return contador

def factorial(n):
    contador = 1
    for k in range(1,  n + 1):
            contador *= k
    return contador
