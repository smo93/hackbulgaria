time_left = 0
is_running = False


def start_timer(time):
    global is_running
    if is_running:
        return False

    global time_left
    time_left = time
    is_running = True


def decrease_time():
    global is_running
    if not is_running:
        return False

    global time_left

    if time_left < 1:
        return False

    time_left -= 1
    return True
