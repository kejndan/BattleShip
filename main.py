from field import Field
from strike import Strike
from comp_enemy import Enemy
from player import Player
__author__ = 'Adel'
if __name__ == '__main__':
    size_field = int(input('Enter the size of the field\n'))
    name_first_player = str(input('Enter the name of the first player\n'))
    name_second_player = str(input('Enter the name of the second player\n'))
    first_player = Player(name_first_player, 1, size_field)
    first_player.field.add_ships(first_player)
    first_player.field.draw(first_player.player_name)
    AI_enemy = Enemy('easy', size_field)
    second_player = Player(name_second_player, 2, size_field)
    AI_enemy.add_ships(second_player)
    second_player.field.draw('Comp')
    # second_player.field.add_ships(second_player)
    # second_player.field.draw(second_player.player_name)
    shoot = Strike()
    point = 0
    while True:
        res = 'K'
        first_player.attack(second_player, shoot)
        if first_player.killed == Field.num_ships:
            print('{} won'.format(first_player.player_name))
            break
        # second_player.attack(first_player, shoot)
        while res == 'K':
            res = AI_enemy.AI_attack(first_player, shoot, point)
            if type(res) == tuple:
                point = res
        if second_player.killed == Field.num_ships:
            print('{} won'.format(first_player.player_name))
            break











