import re

def is_an_bn(word):
    if len(word) % 2 == 0:
        n = int(len(word) / 2)
        m = re.match('a{'+str(n)+'}b{'+str(n)+'}', word)
        if m == None:
            return False
        else:
            return True
    else:
        return False
