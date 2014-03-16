def biggest_difference(arr):
    if not arr == []:
        arr.sort()
        return arr[0] - arr[-1]
    else:
        return False
