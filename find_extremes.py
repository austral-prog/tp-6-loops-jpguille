def find_min(numbers):
    min = numbers[0]
    for n in numbers:
        if n < min:
            min = n
    return min
def find_max(numbers):
    max = numbers[0]
    for n in numbers:
        if n > max:
            max = n
    return max


def count_negatives(numbers):

    cnt = 0
    for n in numbers:
        if n<0:
            cnt += 1
    return cnt
