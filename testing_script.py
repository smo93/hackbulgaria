import os
from subprocess import call, check_output

def find_all_test_files():
    return check_output('find ./ -name test.py', shell=True).decode().splitlines()

def run_test(test_file):
    call('cd {0} && py {1} && cd ..'.format(test_file[:-7], test_file[-7:]), shell=True)

def main():
    test_files = find_all_test_files()
    for test in test_files:
        run_test(test)

if __name__ == '__main__':
    main()
