import re

def reduce_file_path(path):
    new_path = re.sub('\w+/\.\./', '/', path)
    new_path = re.sub('/\.\./', '/', new_path)
    new_path = re.sub('\./', '/', new_path)
    new_path = re.sub('//+', '/', new_path)
    if new_path[-1] == '/' and new_path != '/':
        return new_path[:-1]
    return new_path
