def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        return nth_fib_lists(listB, listA + listB, n - 1)
