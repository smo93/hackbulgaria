def comp_fractions(fr1, fr2):
    f1 = fr1[0] / fr1[1]
    f2 = fr2[0] / fr2[1]
    if f1 < f2:
        return -1
    elif f1 == f2:
        return 0
    else:
        return 1

def sort_fractions(fractions):
    for i in range(len(fractions)):
        min_fr = i
        for j in range(i, len(fractions)):
            if comp_fractions(fractions[j], fractions[min_fr]) == -1:
                min_fr = j
        if i != min_fr:
            tmp = fractions[i]
            fractions[i] = fractions[min_fr]
            fractions[min_fr] = tmp
    return fractions
