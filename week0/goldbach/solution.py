from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    if n > 2 and n % 2 == 0:
        result = []
        for i in range(2, int(n / 2) + 1):
            if is_prime(i) and is_prime(n - i):
                result.append((i, n - i))
        return result
    else:
        return []
