def final_position(command_string, A, B):
    pos = 0
    for ch in command_string:
        if ch == 'L' and pos > -(A):
            pos -= 1
        elif ch == 'R' and pos < B:
            pos += 1
    return pos

