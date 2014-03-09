"""attendance.py"""

from time import time
from datetime import datetime
from glob import glob
from subprocess import call

def parse_command(command):
    """Parses a command string to a tuple"""
    command_tuple = tuple(command.split(' '))
    return command_tuple

def is_command(command_tuple, command_string):
    """Checks if command is valid"""
    return command_tuple[0] == command_string

def save(database_file):
    """Saves the names of attending students from the database_file"""
    file_to_write = open('attendance_' + database_file['date'], 'w')
    file_to_write.write('\n'.join(database_file['attending']))
    file_to_write.close()

def trigger_create(command, database_file, current_date):
    """Checks if a file for the current_date already exists and creates
        new if not"""
    if len(command) > 1:
        print('Too many arguments.\nUse `create` only.\n')
    else:
        filename = "attendance_" + current_date
        if filename in glob(filename):
            print("You already have a file for today. It is: %s"%filename)
        else:
            if not database_file['is_saved']:
                save(database_file)
            database_file.clear()
            database_file['date'] = current_date
            database_file['is_saved'] = True
            database_file['attending'] = []
            call(['touch', filename])
            print("New file created and loaded: %s"%filename)

def trigger_change_date(command, database_file):
    """change_date"""
    if len(command) == 1:
        print('You must specify the new date in a DD/MM/YYYY format.\n')
    elif len(command) > 2:
        print('`change_date` takes only one argument.')
    else:
        new_date = []
        new_date.append(command[1][6:])
        new_date.append(command[1][3:5])
        new_date.append(command[1][:2])

        if not database_file['is_saved']:
            save(database_file)
        database_file.clear()
        database_file['is_saved'] = True

        return "_".join(new_date)

def trigger_add(command, students, database_file):
    """Adds a student to the currently attending students list
        in database_file"""
    if len(command) == 1:
        print('`create` take one argument - a student name.')
    else:
        name = " ".join(command[1:])
    if name in students:
        if not name in database_file['attending']:
            database_file['attending'].append(name)
            database_file['is_saved'] = False
            print('%s is now attending.'%name)
        else:
            print('%s is already attending.'%name)


def trigger_load(command, files, database_file):
    """Loads an attendance file and returns it as a set"""
    if len(command) == 1:
        print('The `load` command must have a file ID as an argument.')
    elif len(command) > 2:
        print('The `load` command takes exactly one argument.')
    else:
        if not database_file['is_saved']:
            save(database_file)

        database_file.clear()

        file_id = int(command[1])
        filename = files[file_id]

        database_file['date'] = filename[11:]
        database_file['is_saved'] = True

        new_file = open(filename, 'r')
        content = new_file.read().splitlines()
        database_file['attending'] = [st for st in content if st != '']
        new_file.close()

def trigger_list(command, files):
    """list_files"""
    if len(command) > 1:
        print('The `list` command takes no arguments.')
    else:
        files_list = glob("attendance_*")
        files.clear()
        for i in range(len(files_list)):
            files[i + 1] = files_list[i]
            print("[%d] - %s"%((i + 1), files_list[i]))

def trigger_status(command, database_file):
    """status"""
    if len(command) > 1:
        print('The `status` command takes no arguments.')
    else:
        if 'attending' in database_file:
            print(database_file['date'])
            for student in database_file['attending']:
                print(student)
        else:
            print('No file loaded.')

def count_students(filename):
    """Get the number of students in the given file"""
    att_file = open(filename, "r")
    list_of_students = [x for x in att_file.read().splitlines() if x != '']
    return len(list_of_students)

def trigger_statistic(command, files_list):
    """statistic"""
    if len(command) > 1:
        print('The `statistic` command takes no arguments.')
    else:
        all_students = count_students('students')
        for filename in list(files_list.values()):
            print('File: %s - %d people attending from total of %d students'
                %(filename[11:], count_students(filename), all_students))

def main():
    """main"""
    timest = time()
    current_date = datetime.fromtimestamp(timest).strftime('%Y_%m_%d')

    students_file = open('students', 'r')
    students = [st for st in students_file.read().splitlines() if st != '']

    files = {}
    database_file = {'is_saved': True}

    while True:
        command = parse_command(input('Enter command >> '))

        if is_command(command, 'create'):
            trigger_create(command, database_file, current_date)
        elif is_command(command, 'change_date'):
            current_date = trigger_change_date(command, database_file)
        elif is_command(command, 'add'):
            trigger_add(command, students, database_file)
        elif is_command(command, 'list'):
            trigger_list(command, files)
        elif is_command(command, 'load'):
            trigger_load(command, files, database_file)
        elif is_command(command, 'status'):
            trigger_status(command, database_file)
        elif is_command(command, 'statistic'):
            trigger_statistic(command, files)
        elif is_command(command, 'exit'):
            if not database_file['is_saved']:
                save(database_file)
            break
        else:
            print('Unknown command.')


if __name__ == '__main__':
    main()
