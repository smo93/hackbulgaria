from time import time
from datetime import datetime
from glob import glob

def add_order(orders, name, price):
    if name in orders:
        orders[name] += price
    else:
        orders[name] = price
    print("Taking order from " + name + " for " + str(price))

def print_status(orders):
    for person in orders:
            print(person + ' - ' + str(orders[person]))

def save(orders):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + stamp
    file = open(filename, "w")
    for person in orders:
        file.write(person + ' - ' + str(orders[person]) + '\n')
    file.close()

def list_order_files():
    files = glob("orders_*")
    dict_of_orders = {}
    for i in range(1, len(files) + 1):
        dict_of_orders[i] = files[i - 1]
    return dict_of_orders

def print_orders_dict(dict_of_orders):
    for i in dict_of_orders:
        print("[" + str(i) + "] - " + dict_of_orders[i])

def load_orders(n, dict_of_orders, orders):
    file = open(dict_of_orders[n], "r")
    content = file.read()
    content = content.splitlines()
    orders.clear()
    for line in content:
        words = line.split()
        orders[words[0]] = float(words[2])

def main():
    orders = {}
    orders_files = list_order_files()
    is_running = True
    is_changed_f = False
    is_changed_l = False

    while is_running:
        command = input("Enter command>")
        spl_cmd = command.split()

        if spl_cmd[0].lower() == "take" and len(spl_cmd) == 3:
            add_order(orders, spl_cmd[1], float(spl_cmd[2]))
            is_changed_l = True
            is_changed_f = True
        elif spl_cmd[0].lower() == "status" and len(spl_cmd) == 1:
            print_status(orders)
        elif spl_cmd[0].lower() == "save" and len(spl_cmd) == 1:
            save(orders)
            is_changed_l = False
            is_changed_f = False
        elif spl_cmd[0].lower() == "list" and len(spl_cmd) == 1:
            orders_files = list_order_files()
            print_orders_dict(orders_files)
        elif spl_cmd[0].lower() == "load" and len(spl_cmd) == 2:
            if is_changed_l:
                print ("You have unsaved order.\n"
                    + "If you wish to discard the current order, type load again.")
                is_changed_l = False
            else:
                load_orders(int(spl_cmd[1]), orders_files, orders)
                is_changed_f = False
                is_changed_l = False
        elif spl_cmd[0].lower() == "finish" and len(spl_cmd) == 1:
            if is_changed_f:
                print ("You have not saved your order.\n"
                    + "If you wish to continue, type finish again.")
                is_changed_f = False
            else:
                is_running = False
        else:
            print("Unknown command!")



if __name__ == "__main__":
    main()