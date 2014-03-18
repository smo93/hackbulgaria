def magic_string(string):
    string = list(string)
    count = 0
    for i in range(int(len(string) / 2)):
        if string[i] != '>':
            string[i] = '>'
            count += 1
        if string[-(i + 1)] != '<':
            string[-(i + 1)] = '>'
            count += 1
    return count

