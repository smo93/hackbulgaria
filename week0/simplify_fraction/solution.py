def simplify_fraction(fraction):
    i = 2
    while i <= fraction[0]:
        while fraction[0] % i == 0 and fraction[1] % i == 0:
            fraction = (int(fraction[0] / i), int(fraction[1] / i))
        i += 1
    return fraction
