def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        return nth_fib_lists(listB, listA + listB, n - 1)

def list_to_number(digits):
    number = 0
    for dig in digits:
        number = number * 10 + dig
    return number


def member_of_nth_fib_lists(listA, listB, needle):
    n = 1
    while True:
        nth = nth_fib_lists(listA, listB, n)
        if len(nth) > len(needle):
            return False
        if nth == needle:
            return True
        n += 1
