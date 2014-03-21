import os


class Dungeon():
    """docstring for Dungeon"""
    def __init__(self):
        if os.path.isfile('maps/level_1.txt'):
            map_file = open('maps/level_1.txt')
            file_content = map_file.read()
            self.map = [list[line] for line in file_content.splitlines()]
            self.level = 1
        else:
            return None

        self.player = None
