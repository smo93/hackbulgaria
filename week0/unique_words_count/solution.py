def count_words(arr):
    result = {}
    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def unique_words_count(arr):
    return len(count_words(arr))
