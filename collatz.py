def collatz_steps(n):

    pasos = 0
    n = int(n)

    while n != 1:
        if n % 2 == 0:
            n = n / 2
            pasos += 1
        else:
            n = (n * 3) + 1
            pasos += 1
    return pasos




def collatz_sequence(n):

    n = int(n)
    sec = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            sec.append(n)
        else:
            n = (n * 3) + 1
            sec.append(n)
    return sec
