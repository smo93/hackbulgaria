import hero, orc, dungeon, weapon
from subprocess import call
from random import randint


def parse_command(command):
    command_tuple = tuple(command.split(' '))
    return command_tuple

def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string

def main():
    call('clear')

    game = dungeon.Dungeon('map.txt')
    
    hero_name = input('Enter your name: ')
    hero_nick = input('Enter your nickname: ')

    player = hero.Hero(hero_name, 100, hero_nick)

    weapons = {}
    weapons[1] = weapon.Weapon('Dagger', 10, 0.6)
    weapons[2] = weapon.Weapon('Sword', 15, 0.3)
    weapons[3] = weapon.Weapon('Mace', 25, 0.1)

    print('Choose your weapon: ')
    for num in weapons:
        print('%d - %s' % (num, weapons[num].type))
    choice = int(input('>'))
    if choice in [1,2,3]:
        player.equip_weapon(weapons[choice])

    game.spawn('player1', player)

    oponent = orc.Orc('The Enemy', 30, 1.3)
    oponent.equip_weapon(weapons[randint(1, 3)])
    oponent1 = orc.Orc('The Enemy1', 30, 1.3)
    oponent1.equip_weapon(weapons[randint(1, 3)])

    game.spawn('enemy', oponent)
    game.spawn('enemy1', oponent1)

    while True:
        call('clear')

        game.print_map()

        command = parse_command(input('Enter command>'))

        if is_command(command, 'move'):
            if command[1] == 'left':
                result = game.move('player1', 'left')
            elif command[1] == 'right':
                result = game.move('player1', 'right')
            elif command[1] == 'up':
                result = game.move('player1', 'up')
            elif command[1] == 'down':
                result = game.move('player1', 'down')
            else:
                print('Wrong direction!')
                input()

            if result == False:
                print('Obstacle in that direction!')
                input()
            elif result == 'H':
                print('You defeated the enemy!')
                input()
                if len(game.players) == 1:
                    print('There are no enemies left!\nYou won!')
                    input()
                    call('clear')
                    break
            elif result == 'O':
                print('Game over!')
                input()
                call('clear')
                break

        elif is_command(command, 'exit'):
            call('clear')
            break
        else:
            print('Wrong command!')
            input()
        
if __name__ == '__main__':
    main()
