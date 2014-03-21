from hero import Hero
from orc import Orc
from fight import Fight


class Dungeon():
    """docstring for Dungeon"""
    def __init__(self, map_path):
        map_file = open(map_path, 'r')
        self.map = map_file.read().splitlines()
        map_file.close()
        self.map = [list(x) for x in self.map]
        self.players = {}

    def print_map(self):
        """docstring for print_map"""
        printing_map = '\n'.join([''.join(x) for x in self.map])
        print(printing_map)
        return printing_map

    def spawn(self, name, entity):
        """docstring for spawn"""
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'S':
                    if type(entity) is Hero:
                        self.map[i][j] = 'H'
                        self.players[name] = [entity, (i, j)]
                        return True
                    elif type(entity) is Orc:
                        self.map[i][j] = 'O'
                        self.players[name] = [entity, (i, j)]
                        return True
                    else:
                        break
        return False

    def move(self, player_id, direction):
        if player_id in self.players:
            pos = self.players[player_id][1]
            new_pos = ()

            oponent = 'O' if type(self.players[player_id][0]) is Hero else 'H'

            if direction == 'right' and pos[1] + 1 < len(self.map[pos[0]]):
                new_pos = (pos[0], pos[1] + 1)

            elif direction == 'left' and pos[1] - 1 >= 0:
                new_pos = (pos[0], pos[1] - 1)

            elif direction == 'up' and pos[0] - 1 >= 0:
                new_pos = (pos[0] - 1, pos[1])

            elif direction == 'down' and pos[0] + 1 < len(self.map):
                new_pos = (pos[0] + 1, pos[1])

            else:
                return False

            if self.map[new_pos[0]][new_pos[1]] == '.':
                self.map[new_pos[0]][new_pos[1]] = self.map[pos[0]][pos[1]]
                self.map[pos[0]][pos[1]] = '.'
                self.players[player_id][1] = new_pos
                return True

            elif self.map[new_pos[0]][new_pos[1]] == oponent:
                for oponent_name in self.players:

                    if self.players[oponent_name][1] == new_pos:
                        fight = Fight(self.players[player_id][0], self.players[oponent_name][0])

                        if not fight is None:
                            fight_outcome = fight.simulate_fight()
                            print(fight_outcome[0])

                            if fight_outcome[1] == 'H':
                                self.players.pop(oponent_name)
                                self.players[player_id][1] = new_pos
                                self.map[new_pos[0]][new_pos[1]] = self.map[pos[0]][pos[1]]
                                self.map[pos[0]][pos[1]] = '.'

                            elif fight_outcome[1] == 'O':
                                self.players.pop(player_id)
                                self.map[pos[0]][pos[1]] = '.'

                            return fight_outcome[1]
            else:
                return False

